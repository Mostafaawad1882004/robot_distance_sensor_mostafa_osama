"""
Program: Robot Distance Sensor Controller
Description: This program reads a list of distance measurements from a robot's 
             front sensor and decides the appropriate movement action for each 
             reading while handling potential input errors and monitoring battery.
Author: Moustafa Osama
"""

class Robot:
    def __init__(self, name: str, battery: int = 100):
        """
        Initializes the Robot object with a name and a battery percentage.
        """
        self.name = name
        self.battery = battery

    def process_distances(self, distance_list: list) -> list:
        """
        Processes a list of distance readings and returns a list of recommended actions.
        - Less than 0.5m: STOP
        - Between 0.5m and 1.0m: SLOW
        - More than 1.0m: MOVE FAST
        Includes Error Handling for invalid data types or negative distances.
        """
        actions = []
        
        # Validation: Ensure the input is a valid list
        if not isinstance(distance_list, list):
            print("Error: Input must be a list of numbers.")
            return ["ERROR_INVALID_INPUT"]

        for distance in distance_list:
            try:
                # Convert the reading to float to ensure numeric processing
                dist_float = float(distance)
                
                # Check for physical anomalies (Negative distances)
                if dist_float < 0:
                    actions.append("ERROR (Negative Distance)")
                    continue
                
                # Apply distance-based decision logic
                if dist_float < 0.5:
                    actions.append("STOP")
                elif 0.5 <= dist_float <= 1.0:
                    actions.append("SLOW")
                else:
                    actions.append("MOVE FAST")
                    
            except (ValueError, TypeError):
                # Handle corrupted or non-numeric elements gracefully without crashing
                actions.append("ERROR (Invalid Value)")
                
        return actions


# ==========================================
# TEST CODE (Required Assignment Test Cases)
# ==========================================
if __name__ == "__main__":
    # Create an instance of the Robot class
    my_robot = Robot(name="RoboNav-3", battery=95)
    print(f"--- Testing Robot: {my_robot.name} (Battery: {my_robot.battery}%) ---")
    
    # Test Case 1: Standard readings provided in the assignment example
    test_case_1 = [0.3, 1.5, 0.8, 2.0, 0.4]
    print(f"Test 1 (Standard): Input {test_case_1}")
    print(f"Result: {my_robot.process_distances(test_case_1)}\n")
    
    # Test Case 2: Exact boundary coordinates (Edge Cases)
    test_case_2 = [0.5, 1.0, 0.0]
    print(f"Test 2 (Edge Cases): Input {test_case_2}")
    print(f"Result: {my_robot.process_distances(test_case_2)}\n")
    
    # Test Case 3: Error handling checks (Strings and negative bounds)
    test_case_3 = [1.2, -0.4, "bad_data", 0.7]
    print(f"Test 3 (Error Handling): Input {test_case_3}")
    print(f"Result: {my_robot.process_distances(test_case_3)}\n")
    
    # Test Case 4: Long clear range paths
    test_case_4 = [5.5, 10.0, 0.2]
    print(f"Test 4 (Clear Path): Input {test_case_4}")
    print(f"Result: {my_robot.process_distances(test_case_4)}\n")
    
    # Test Case 5: Empty readings check
    test_case_5 = []
    print(f"Test 5 (Empty List): Input {test_case_5}")
    print(f"Result: {my_robot.process_distances(test_case_5)}\n")