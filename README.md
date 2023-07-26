## Traffic Light Expert System

This is a simple expert system for simulating a traffic light using Python and the `experta` library. The expert system is designed to provide responses based on the color input provided by the user.

### Prerequisites

Before running the code, make sure you have the following installed:

- Python (version X.X or higher) - [Download Python](https://www.python.org/downloads/)

### Installation

1. Clone this repository to your local machine or download the code as a ZIP file.
2. Navigate to the project directory.

### Usage

To run the Traffic Light Expert System, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory where the `expert_system_traffic_light.py` file is located.
3. Run the following command:

```
python expert_system_traffic_light.py
```

4. The program will prompt you to enter the color of the traffic light (red, green, or yellow).
5. Type your choice and press Enter.
6. The expert system will then provide an appropriate response based on the input color.

### Example

```
$ python expert_system_traffic_light.py
Enter your color (red, green, yellow): green
Go. The traffic light is green.
```

### How It Works

The expert system is based on the `experta` library, which provides a rule-based engine for defining and processing knowledge. The `TrafficLigthExpertSystem` class is defined, which extends the `KnowledgeEngine` class from `experta`.

The expert system uses rules to match the color input and provide the corresponding response for each color:

- If the color is "red," it prints "stop. the traffic light is red."
- If the color is "yellow," it prints "prepare to stop. the traffic light is yellow."
- If the color is "green," it prints "Go. the traffic light is green."

The `traffic_light_system` instance is created, and the `reset()` method is called to initialize the expert system. Then, the `run()` method is invoked to start the inference process.

### Customization

Feel free to customize the expert system's responses or add more rules and facts to extend its functionality. For example, you could incorporate additional conditions or logic to simulate a more complex traffic light system.

### License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

---

Happy coding!
