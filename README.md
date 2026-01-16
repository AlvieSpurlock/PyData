# PyData

A lightweight data‑management layer that accepts Python dictionaries and consolidates them into clean, readable .txt files using the PyConsole formatting system.

## Overview

PyData acts as the bridge between raw structured data and human‑readable output.It stores data internally using PyTable, formats it using PyConsole, and writes the final consolidated output to disk.

This makes PyData ideal for:

- CLI Tools

- Debugging Utilities

- Text‑based Engines

- Data Inspection

- Developer‑facing Tools

Its output is structured, visually consistent, and easy to scan.

## Why PyData?
PyData exists to solve a simple but common problem: turning raw Python data into clean, readable, structured output without building a full database or writing repetitive formatting code. It gives you a lightweight, modular way to store, update, and visualize data using a consistent console‑style layout. Instead of juggling print statements, manual formatting, or ad‑hoc text files, PyData handles the entire pipeline — storage, formatting, and persistence — with a single, predictable interface.

## Core Features

### Dictionary‑First Input

PyData accepts dictionaries as its primary data format. Each key/value pair becomes a labeled field in the final output.

### Automatic Consolidation

Every time you add, replace, or remove data, PyData regenerates a fully formatted .txt file that reflects the current state of the dataset.

### PyConsole Formatting

PyData uses PyConsole’s visual language:

1. PrintHeader for dataset titles

2. PrintSubHeader for per‑entry labels

3. PrintNumberedList or PrintList for fields

4. PrintSubHeader("") as a visual breaker

This creates a clean, section‑based layout.

### Flexible Field Formatting

The useIndex flag lets you choose between:

- Numbered fields (1, 2, 3…)

- Plain fields (no numbering)

Useful for debugging, menus, or simple data dumps.

### Modular Architecture

PyData delegates:

- Storage → PyTable

- Formatting → PyConsole

- Persistence → SaveData

This keeps responsibilities clean and the system easy to extend.

## Example


#### Input dictionary:
```python
{
    "Name": "Potion",
    "Heals": 25,
    "Type": "Consumable"
}
```

#### Output (Items.txt), if useIndex is True:
```txt
||=====[Items]=====||

[---[Potion]---]

1 - Name: Potion
2 - Heals: 25
3 - Type: Consumable

[---[==]---]
```
#### Output (Items.txt), if useIndex is False:
```txt
||=====[Items]=====||

[---[Potion]---]

Name: Potion<br>
Heals: 25<br>
Type: Consumable<br>

[---[==]---]
```
### Class Structure
```python
class PyData:

    def __init__(self, dataName, data):
        self.name = dataName
        self.table = PyTable(data)

    def AddData(self, data, nameIndex, useIndex):
        self.table.AddItem(data)
        self.SaveData(self.ConsolidateData(nameIndex, useIndex))

    def ReplaceData(self, i, data, nameIndex, useIndex):
        self.table.ReplaceItem(i, data)
        self.SaveData(self.ConsolidateData(nameIndex, useIndex))

    def RemoveItem(self, i):
        self.table.RemoveItem(i)

    def ConsolidateData(self, nameIndex, useIndex):
        ...
        return consolidated_output

    def SaveData(self, data):
        with open(f"{self.name}.txt", "w+") as dataFile:
            dataFile.write(data)
```
### Usage Example
```python
items = PyData("Items", {
    "Name": "Potion",
    "Heals": 25,
    "Type": "Consumable"
})

items.AddData({
    "Name": "Elixir",
    "Heals": 100,
    "Type": "Rare Consumable"
}, nameIndex="Name", useIndex=True)
```
This automatically regenerates Items.txt with both entries formatted.

## Summary

PyData transforms structured Python dictionaries into clean, readable .txt files using a consistent console‑style formatting system. It updates automatically on every change, making it a reliable component for CLI tools, debugging suites, and text‑based engines.

Requires: Python 3.x, PyTable, PyConsole
