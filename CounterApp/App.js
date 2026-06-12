import { useState } from "react";
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  StatusBar,
  SafeAreaView,
} from "react-native";

export default function App() {
  const [count, setCount] = useState(0);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const handleIncrement = () => setCount((prev) => prev + 1);

  const handleDecrement = () => {
    if (count > 0) setCount((prev) => prev - 1); // never go below 0
  };

  const handleReset = () => setCount(0);

  const toggleTheme = () => setIsDarkMode((prev) => !prev);

  const theme = isDarkMode ? darkTheme : lightTheme;

  return (
    <SafeAreaView style={[styles.safeArea, { backgroundColor: theme.background }]}>
      <StatusBar
        barStyle={isDarkMode ? "light-content" : "dark-content"}
        backgroundColor={theme.background}
      />

      <View style={[styles.container, { backgroundColor: theme.background }]}>

        <Text style={[styles.title, { color: theme.textPrimary }]}>
          Counter App
        </Text>
        <Text style={[styles.subtitle, { color: theme.textSecondary }]}>
          {isDarkMode ? "🌙 Dark Mode" : "☀️ Light Mode"}
        </Text>

        <View
          style={[
            styles.counterCard,
            { backgroundColor: theme.card, shadowColor: theme.shadow },
          ]}
        >
          <Text style={[styles.counterLabel, { color: theme.textSecondary }]}>
            CURRENT COUNT
          </Text>
          <Text
            style={[
              styles.counterValue,
              { color: count === 0 ? theme.textSecondary : theme.accent },
            ]}
          >
            {count}
          </Text>
          {count === 0 && (
            <Text style={[styles.zeroHint, { color: theme.textSecondary }]}>
              Tap + to get started
            </Text>
          )}
        </View>

        <View style={styles.row}>
          <TouchableOpacity
            style={[
              styles.actionButton,
              {
                backgroundColor:
                  count === 0 ? theme.disabledBg : theme.decrementBg,
              },
            ]}
            onPress={handleDecrement}
            disabled={count === 0}
            activeOpacity={0.75}
          >
            <Text
              style={[
                styles.actionButtonIcon,
                {
                  color:
                    count === 0 ? theme.disabledText : theme.decrementText,
                },
              ]}
            >
              −
            </Text>
            <Text
              style={[
                styles.actionButtonLabel,
                {
                  color:
                    count === 0 ? theme.disabledText : theme.decrementText,
                },
              ]}
            >
              Decrement
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[
              styles.actionButton,
              { backgroundColor: theme.incrementBg },
            ]}
            onPress={handleIncrement}
            activeOpacity={0.75}
          >
            <Text
              style={[styles.actionButtonIcon, { color: theme.incrementText }]}
            >
              +
            </Text>
            <Text
              style={[
                styles.actionButtonLabel,
                { color: theme.incrementText },
              ]}
            >
              Increment
            </Text>
          </TouchableOpacity>
        </View>

        <TouchableOpacity
          style={[
            styles.resetButton,
            {
              backgroundColor: theme.resetBg,
              borderColor: theme.resetBorder,
            },
          ]}
          onPress={handleReset}
          activeOpacity={0.75}
        >
          <Text style={[styles.resetButtonText, { color: theme.resetText }]}>
            ↺  Reset
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.themeButton, { backgroundColor: theme.themeBg }]}
          onPress={toggleTheme}
          activeOpacity={0.8}
        >
          <Text style={[styles.themeButtonText, { color: theme.themeText }]}>
            {isDarkMode ? "☀️  Switch to Light Mode" : "🌙  Switch to Dark Mode"}
          </Text>
        </TouchableOpacity>

      </View>
    </SafeAreaView>
  );
}

const lightTheme = {
  background: "#F5F7FA",
  card: "#FFFFFF",
  shadow: "#000",
  textPrimary: "#1A1D23",
  textSecondary: "#8A8FA8",
  accent: "#4F6EF7",
  incrementBg: "#4F6EF7",
  incrementText: "#FFFFFF",
  decrementBg: "#FFF0F0",
  decrementText: "#E53E3E",
  disabledBg: "#EAECF0",
  disabledText: "#BEC3D0",
  resetBg: "#FFFFFF",
  resetBorder: "#D1D5E0",
  resetText: "#4A4F63",
  themeBg: "#1A1D23",
  themeText: "#FFFFFF",
};

const darkTheme = {
  background: "#0F1117",
  card: "#1C1F2E",
  shadow: "#000",
  textPrimary: "#E8EAF2",
  textSecondary: "#5C627A",
  accent: "#7B96FF",
  incrementBg: "#2D3A6B",
  incrementText: "#A5B8FF",
  decrementBg: "#2D1F1F",
  decrementText: "#FF7070",
  disabledBg: "#1C1F2E",
  disabledText: "#3A3F52",
  resetBg: "#1C1F2E",
  resetBorder: "#2C3050",
  resetText: "#8A8FA8",
  themeBg: "#E8EAF2",
  themeText: "#1A1D23",
};

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
  },
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    paddingHorizontal: 28,
    paddingVertical: 24,
  },

  title: {
    fontSize: 30,
    fontWeight: "800",
    letterSpacing: 0.5,
    marginBottom: 4,
  },
  subtitle: {
    fontSize: 14,
    fontWeight: "500",
    marginBottom: 40,
    letterSpacing: 0.3,
  },

  counterCard: {
    width: "100%",
    alignItems: "center",
    paddingVertical: 40,
    borderRadius: 24,
    marginBottom: 36,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.08,
    shadowRadius: 16,
    elevation: 5,
  },
  counterLabel: {
    fontSize: 11,
    fontWeight: "700",
    letterSpacing: 2,
    marginBottom: 12,
  },
  counterValue: {
    fontSize: 80,
    fontWeight: "800",
    lineHeight: 90,
  },
  zeroHint: {
    marginTop: 8,
    fontSize: 13,
    fontWeight: "400",
  },

  row: {
    flexDirection: "row",
    gap: 14,
    width: "100%",
    marginBottom: 14,
  },
  actionButton: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    paddingVertical: 20,
    borderRadius: 18,
  },
  actionButtonIcon: {
    fontSize: 28,
    fontWeight: "700",
    lineHeight: 32,
  },
  actionButtonLabel: {
    fontSize: 12,
    fontWeight: "600",
    marginTop: 2,
    letterSpacing: 0.3,
  },

  resetButton: {
    width: "100%",
    alignItems: "center",
    paddingVertical: 16,
    borderRadius: 18,
    borderWidth: 1.5,
    marginBottom: 14,
  },
  resetButtonText: {
    fontSize: 15,
    fontWeight: "600",
    letterSpacing: 0.4,
  },

  themeButton: {
    width: "100%",
    alignItems: "center",
    paddingVertical: 16,
    borderRadius: 18,
  },
  themeButtonText: {
    fontSize: 15,
    fontWeight: "700",
    letterSpacing: 0.4,
  },
});