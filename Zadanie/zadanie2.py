#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import click


def adding(flights, stay, number, value, file_name):
    """
    Добавление нового рейса
    """
    flights.append(
        {
            'stay': stay,
            'number': number,
            'value': value
        }
    )
    with open(file_name, "w", encoding="utf-8") as file_out:
        json.dump(flights, file_out, ensure_ascii=False, indent=4)
    click.secho('Рейс добавлен', fg='green')
    return flights


def table(line, flights):
    """Вывод скиска рейсов"""
    print(line)
    print(
        '| {:^4} | {:^20} | {:^15} | {:^16} |'.format(
            "№",
            "Место прибытия",
            "Номер самолёта",
            "Тип"))
    print(line)
    for i, num in enumerate(flights, 1):
        print(
            '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                i,
                num.get('stay', ''),
                num.get('number', ''),
                num.get('value', 0)
            )
        )
    print(line)


def selecting(line, flights, nom):
    """Выбор рейсов по типу самолёта"""
    count = 0
    print(line)
    print(
        '| {:^4} | {:^20} | {:^15} | {:^16} |'.format(
            "№",
            "Место прибытия",
            "Номер самолёта",
            "Тип"))
    print(line)
    for i, num in enumerate(flights, 1):
        if nom == num.get('value', ''):
            count += 1
            print(
                '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                    count,
                    num.get('stay', ''),
                    num.get('number', ''),
                    num.get('value', 0)))
    print(line)


def opening(file_name):
    with open(file_name, "r", encoding="utf-8") as f_in:
        return json.load(f_in)


@click.command()
@click.option("-c", "--command")
@click.argument('filename')
@click.option("-s", "--stay")
@click.option("-v", "--value")
@click.option("-n", "--number")
@click.option("-t", "--typing")
def main(command, filename, stay, value, number, typing):
    flights = opening(filename)
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 20,
        '-' * 15,
        '-' * 16
    )
    if command == 'add':
        adding(flights, stay, number, value, filename)
    elif command == 'display':
        table(line, flights)
    elif command == 'select':
        selecting(line, flights, typing)


if __name__ == '__main__':
    main()
