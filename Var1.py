import time
import threading

# Dictionary for urine color health insights and recommended water intake
urine_color_info = {
    'clear': {
        'meaning': 'You are well hydrated, but you may be drinking too much water.',
        'risk': 'Overhydration can dilute essential salts in your body.',
        'water_needed': 0.5  # Liters to drink
    },
    'pale yellow': {
        'meaning': 'This is a healthy color, indicating proper hydration.',
        'risk': 'No risks, you’re doing well!',
        'water_needed': 0.3  # Liters to drink
    },
    'dark yellow': {
        'meaning': 'You are slightly dehydrated.',
        'risk': 'May lead to dehydration if not addressed.',
        'water_needed': 1.0  # Liters to drink
    },
    'amber': {
        'meaning': 'You are dehydrated and need water.',
        'risk': 'Dehydration can affect your kidney function and energy levels.',
        'water_needed': 1.5  # Liters to drink
    },
    'brown': {
        'meaning': 'You might have severe dehydration or liver issues.',
        'risk': 'This could indicate liver disease or severe dehydration. Seek medical advice.',
        'water_needed': 2.0  # Liters to drink
    },
    'pink/red': {
        'meaning': 'There might be blood in your urine.',
        'risk': 'This could be a sign of infection, kidney issues, or even more serious conditions. Seek medical attention.',
        'water_needed': 1.5  # Liters to drink, plus see a doctor
    }
}

# Function to determine health insights based on urine color
def get_urine_health_insights(color):
    if color in urine_color_info:
        return urine_color_info[color]
    else:
        return {
            'meaning': 'Unknown color. Please consult a doctor if this persists.',
            'risk': 'This urine color is not typical, so it’s hard to give advice without medical consultation.',
            'water_needed': 1.0  # Default water intake recommendation
        }

# Function to set reminders at intervals
def water_reminder(interval_in_minutes, water_needed):
    total_time = water_needed * 60  # Reminder for the duration of recommended water consumption
    elapsed_time = 0
    print(f"You need to drink {water_needed} liters of water.")
    while elapsed_time < total_time:
        time.sleep(interval_in_minutes * 60)
        elapsed_time += interval_in_minutes
        print(f"Reminder: Drink water! {elapsed_time} minutes passed.")

# Main app logic
def urine_app():
    print("Welcome to the Urine Health App!")
    print("Please enter the color of your urine from the following options:")
    print("clear, pale yellow, dark yellow, amber, brown, pink/red")
    
    urine_color = input("Enter your urine color: ").lower()
    
    # Get health insights based on urine color
    health_info = get_urine_health_insights(urine_color)
    
    print("\nHealth Insights:")
    print(f"Meaning: {health_info['meaning']}")
    print(f"Potential Risks: {health_info['risk']}")
    
    # Calculate water intake
    water_needed = health_info['water_needed']
    print(f"Recommended Water Intake: {water_needed} liters\n")
    
    # Ask user if they want to set water reminders
    set_reminders = input("Would you like to set water drinking reminders? (yes/no): ").lower()
    if set_reminders == 'yes':
        interval = int(input("Enter reminder interval in minutes: "))
        print(f"Setting reminders every {interval} minutes to drink water...\n")
        
        # Set up water reminders on a separate thread so the user can continue using the app
        reminder_thread = threading.Thread(target=water_reminder, args=(interval, water_needed))
        reminder_thread.start()
    else:
        print("No reminders set. Stay hydrated!\n")

# Run the app
if __name__ == "__main__":
    urine_app()
