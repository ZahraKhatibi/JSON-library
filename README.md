# JSON Parsing and Formatting Script

## Overview

This Python script is designed to parse and format JSON (JavaScript Object Notation) strings for better readability and validation. JSON is a widely used data interchange format for representing structured data, and this script provides a means to ensure the validity and proper formatting of JSON data.

## Features

- **JSON Validation**: The script validates the provided JSON string for correctness, ensuring that it adheres to JSON syntax rules.

- **JSON Formatting**: It formats the JSON data to be more human-readable and indented properly, making it easier to understand and work with.

- **Error Handling**: The script provides error handling for invalid JSON data, raising errors when issues are detected.

## Usage

To use this script, follow these steps:

1. Run the script in a Python environment.

2. Input a JSON string when prompted.

3. The script will validate the JSON string for correctness and format it for improved readability.

4. The formatted JSON data will be displayed in the console.

## Script Structure

- **Global Functions**: The script includes several global functions for validating and formatting JSON data.

- **`quit()`:** Exits the script with an optional message.

- **`checkNum()`:** Checks if a substring represents a valid number.

- **`checkBool()`:** Checks if a substring represents a valid boolean value.

- **`checkArr()`:** Checks if a substring represents a valid JSON array.

- **`checkObj()`:** Checks if a substring represents a valid JSON object.

- **`Print()`:** Formats and prints the JSON data.

- **Main Code**: The main code block reads input, removes spaces, adds brackets if necessary, and utilizes global functions to validate and format the JSON data.

## Dependencies

This script does not have any external dependencies and can be run in any Python environment.

## Error Handling

The script provides error handling for various JSON-related issues, such as invalid syntax, unexpected characters, and mismatched brackets. If an error is detected, the script will exit and display an error message.

## License

This JSON Parsing and Formatting Script is open-source and available under the [insert license here]. Please refer to the LICENSE file for details on usage and distribution.

Please replace "[insert license here]" in the License section with the actual license information for your script.