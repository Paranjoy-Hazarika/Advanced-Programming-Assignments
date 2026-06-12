# Assignment 19: [Counter App]

This branch contains the solutions for the assignment 19.

## Problem Statement
Build a single-screen mobile application using React Native. The app functions as a digital counter that allows users to increment, decrement, and reset a number displayed on the screen. To make the app more interactive, it must also include a "Theme Toggle" button that switches the screen's background and text colors between a Light Mode and a Dark Mode.

This assignment focuses on your ability to set up a basic React Native environment, layout components cleanly using Flexbox, and manage UI changes dynamically using React's state management.

Implementation Rules

Core Layout: The application must use standard React Native components: View, Text, and TouchableOpacity (or Button). The counter UI should be perfectly centered on the screen.

State Management: Use the useState hook to manage two pieces of state: the current counter value (integer) and the active theme mode (boolean or string).

Counter Logic: * The counter should start at 0.

The "Increment" button must increase the count by 1.

The "Decrement" button must decrease the count by 1, but it should never let the counter go below 0 (prevent negative numbers).

The "Reset" button must bring the count back to 0.

Dynamic Styling: * Light Mode (Default): White background with dark text.

Dark Mode: Dark gray/black background with white text.

Clicking the "Toggle Theme" button should instantly swap these styles across the entire screen.

You must have the followings: 
1. UI Layout & Component Structure: Correctly structure the app using a parent container, a text display for the counter, and a clean arrangement of buttons using Flexbox (e.g., placing the increment/decrement buttons side-by-side). 
Use proper React Native style properties (flex, justifyContent, alignItems, fontSize, padding).

2. Counter State & Validation Logic: Successfully implement the useState hook to track and dynamically display the counter value. Implement the increase, decrease, and reset functions correctly. 
Constraint Check: Add an internal conditional check to ensure that clicking decrement at 0 does nothing, keeping the app safe from negative values.

3. Dynamic Theme Toggling: Implement state tracking for the theme (e.g., isDarkMode). Use conditional styling or ternary operators within your style objects to alter the backgroundColor of the main container and the color of the text components based on the theme state.

4. Code Cleanliness & Best Practices: Maintain well-organized code with proper component separation or readable inline styling. Use meaningful variable and function names (e.g., handleIncrement, toggleTheme). 

Ensure no obvious runtime crashes occur during interactions.

Those who are having android mobile must run it in the mobile in development mode. Those having iphone may run in emulator of android studio.

**📱 Testing Method**: Run via the Expo Go Application.

## Video Demonstration

Here is a full screen recording of the application running live on an Android device via Expo Go, demonstrating the counter logic, zero-boundary validation, and the dark mode theme toggle:

**Counter App Demo**
<video width="300" height="400" controls>
    <source src="/Recordings/counter app.mp4" type="video/mp4">
</video>

> 💡 **Note:** If the video does not play automatically in your browser, you can view the raw file directly in the repository [here](./Recordings/counter%20app.mp4).

## Features
- **Increment Functionality:** Increases the counter value with instantaneous UI re-render.
- **Decrement Functionality:** Decreases the counter value.
- **Reset Functionality:** Instantly clears the tracking variable and restores state to `0`.
- **Mobile-First Layout:** Designed using native flexbox styling tailored for physical devices.

## Tech Used
- React Native
- Expo CLI (Latest)

## How to run locally
```bash
git clone https://github.com/Paranjoy-Hazarika/Advanced-Programming-Assignments.git
git checkout assignment-19

cd CounterApp

# Install native dependencies
npm install
# Spin up the local development server
npx expo start