# Nike Inventory Manager

This project is a Python-based inventory management system for Nike shoes.  
It reads and updates stock information stored in a text file (`inventory.txt`) and provides a menu-driven interface for managing shoe data.

## Features

- **View all shoes** currently in stock  
- **Add new shoes** to the inventory  
- **Restock** the item with the lowest quantity  
- **Search** for a shoe using its product code  
- **Calculate total value** for each shoe (cost × quantity)  
- **Identify the product** with the highest stock  

## How It Works

The program loads shoe information from `inventory.txt` on startup, processes it, and allows the user to interact with the data using various menu options. It uses a `Shoe` class to store details for each item.

## Files Included

- `inventory.py` — Main Python program  
- `inventory.txt` — Data file containing shoe stock information  

## Purpose

This project demonstrates basic file handling, classes, lists, and user interaction in Python while simulating a real-world stock management system.
