import streamlit as st
import math
import string
import matplotlib.pyplot as plt

# ------------------------------
# Helper Functions
# ------------------------------

def calculate_entropy(password: str) -> float:
    """Calculate password entropy based on character sets used."""
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)

    if charset_size == 0:
        return 0

    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)


def bruteforce_time(entropy: float) -> float:
    """Estimate brute force crack time in seconds."""
    guesses = 2 ** entropy
    guesses_per_second = 1e9  # Assume 1 billion guesses/sec
    seconds = guesses / guesses_per_second
    return seconds


def convert_time(seconds: float) -> str:
    """Convert seconds into human-readable format."""
    minute = 60
    hour = 3600
    day = 86400
    year = 31557600
    century = year * 100

    if seconds < minute:
        return f"{seconds:.2f} seconds"
    elif seconds < hour:
        return f"{seconds / minute:.2f} minutes"
    elif seconds < day:
        return f"{seconds / hour:.2f} hours"
    elif seconds < year:
        return f"{seconds / day:.2f} days"
    elif seconds < century:
        return f"{seconds / year:.2f} years"
    else:
        return f"{seconds / century:.2f} centuries"


# ------------------------------
# Streamlit App UI
# ------------------------------

st.set_page_config(page_title="CyberGuard - Password Analyzer", page_icon="🔐", layout="wide")

st.title("🔐 CyberGuard - Password Analyzer & Brute Force Estimator")
st.write("Analyze password strength using entropy and estimate brute-force crack time.")

# Input
password = st.text_input("Enter a password:")

if password:
    # Calculate
    entropy = calculate_entropy(password)
    seconds = bruteforce_time(entropy)
    readable_time = convert_time(seconds)

    # Display results
    st.subheader("🔎 Analysis Result")
    st.write(f"**Entropy:** {entropy} bits")
    st.write(f"**Estimated crack time:** {readable_time}")

    # Strength evaluation
    if entropy < 28:
        st.error("❌ Very Weak – Easily crackable")
    elif entropy < 36:
        st.warning("⚠ Weak – Could be cracked quickly")
    elif entropy < 60:
        st.info("🛡 Moderate – Better but still breakable")
    else:
        st.success("✅ Strong – Resistant to brute force")

    # Chart (Entropy vs Password Length)
    lengths = list(range(1, 21))
    entropies = [calculate_entropy(password[:i] + "a"*(i-len(password))) for i in lengths]

    fig, ax = plt.subplots()
    ax.plot(lengths, entropies, marker="o")
    ax.set_title("Entropy Growth with Password Length")
    ax.set_xlabel("Password Length")
    ax.set_ylabel("Entropy (bits)")
    st.pyplot(fig)

else:
    st.info("👆 Enter a password above to analyze.")
