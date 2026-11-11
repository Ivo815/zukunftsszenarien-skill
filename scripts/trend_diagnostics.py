#!/usr/bin/env python3
"""Describe a time,value CSV without forecasting or assigning a growth model."""

import argparse
import csv
import json
import math
import sys


def finite(value, label):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f'{label}: Wert muss endlich sein.')
    return value


def read_points(path):
    points = []
    with open(path, encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not {'time', 'value'} <= set(reader.fieldnames):
            raise ValueError('CSV benötigt die Spalten time,value.')
        for line, row in enumerate(reader, start=2):
            try:
                points.append((finite(row['time'], 'time'), finite(row['value'], 'value')))
            except (ValueError, TypeError, KeyError) as exc:
                raise ValueError(f'CSV-Zeile {line}: ungültiger oder fehlender Wert.') from exc
    return points


def diagnose(points, time_unit='Zeiteinheiten', value_unit='Werteinheiten'):
    points = sorted((finite(t, 'time'), finite(v, 'value')) for t, v in points)
    if len(points) < 2:
        raise ValueError('Mindestens zwei Beobachtungen erforderlich.')
    if any(t1 == t0 for (t0, _), (t1, _) in zip(points, points[1:])):
        raise ValueError('Doppelte Zeitpunkte sind nicht zulässig.')

    positive = all(v > 0 for _, v in points)
    warnings = [
        'Deskriptiv, keine Prognose und keine automatische Kurvenklassifikation.',
        'Einheiten, Vergleichbarkeit, Datenunsicherheit und Wirkmechanismen extern prüfen.',
        'Kein Signifikanztest; Veränderungen können Messfehler oder Stichprobenwechsel abbilden.',
    ]
    if len(points) < 3:
        warnings.append('Zwei Punkte erlauben keine Beschleunigungsdiagnose.')
    if not positive:
        warnings.append('Nichtpositive Werte: relative/geometrische/logarithmische Wachstumsdiagnostik ausgesetzt.')

    intervals = []
    for (t0, v0), (t1, v1) in zip(points, points[1:]):
        dt = t1 - t0
        delta = v1 - v0
        item = {
            'start': t0, 'end': t1, 'duration': dt,
            'absolute_change': delta,
            'absolute_change_per_time_unit': delta / dt,
        }
        if positive:
            log_rate = (math.log(v1) - math.log(v0)) / dt
            item.update({
                'relative_change_over_interval': math.expm1(math.log(v1) - math.log(v0)),
                'log_growth_per_time_unit': log_rate,
                'geometric_growth_per_time_unit': math.expm1(log_rate),
            })
        intervals.append(item)

    rate_changes = []
    for earlier, later in zip(intervals, intervals[1:]):
        first_mid = earlier['start'] + earlier['duration'] / 2
        next_mid = later['start'] + later['duration'] / 2
        midpoint_gap = next_mid - first_mid
        item = {
            'at_time': earlier['end'],
            'change_in_absolute_rate_per_time_unit': (
                later['absolute_change_per_time_unit'] - earlier['absolute_change_per_time_unit']
            ) / midpoint_gap,
        }
        if positive:
            item['change_in_log_growth_rate_per_time_unit'] = (
                later['log_growth_per_time_unit'] - earlier['log_growth_per_time_unit']
            ) / midpoint_gap
        rate_changes.append(item)

    duration = points[-1][0] - points[0][0]
    summary = {
        'start_time': points[0][0], 'end_time': points[-1][0],
        'observations': len(points), 'duration': duration,
        'absolute_change': points[-1][1] - points[0][1],
        'average_absolute_change_per_time_unit': (points[-1][1] - points[0][1]) / duration,
    }
    if positive:
        summary['endpoint_geometric_growth_per_time_unit'] = math.expm1(
            (math.log(points[-1][1]) - math.log(points[0][1])) / duration
        )
        warnings.append('Endpunkt-Wachstum mittelt den Zeitraum; es beweist keine konstante relative Rate.')

    result = {
        'units': {'time': time_unit, 'value': value_unit},
        'summary': summary, 'intervals': intervals,
        'descriptive_rate_changes': rate_changes,
        'growth_rates_are_fractions_not_percent': True,
        'warnings': warnings,
    }
    # Reject overflows, including those produced by subtraction or division.
    json.dumps(result, allow_nan=False)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_path')
    parser.add_argument('--time-unit', default='Zeiteinheiten')
    parser.add_argument('--value-unit', default='Werteinheiten')
    args = parser.parse_args()
    try:
        result = diagnose(read_points(args.csv_path), args.time_unit, args.value_unit)
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (OSError, ValueError, OverflowError, ZeroDivisionError) as exc:
        print(f'Fehler: {exc}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
