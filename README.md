# 🚲 Citi Bike Membership Cost Checker

A comprehensive Streamlit web application that helps you determine whether a Citi Bike annual membership is financially worth it based on your personal riding habits and preferences.

## 📋 Table of Contents

- [🎯 Purpose](#-purpose)
- [✨ Features](#-features)
- [💡 How It Works](#-how-it-works)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [🎮 Usage Guide](#-usage-guide)
- [🧮 Calculation Logic](#-calculation-logic)
- [📊 Understanding Your Results](#-understanding-your-results)
- [🔧 Technical Details](#-technical-details)
- [🐛 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🎯 Purpose

Deciding whether to purchase a Citi Bike annual membership can be tricky. This app eliminates the guesswork by:

- **Calculating precise annual costs** for both membership and pay-per-ride scenarios
- **Accounting for complex pricing rules** including e-bike charges, time limits, and Manhattan caps
- **Providing personalized recommendations** based on your specific riding patterns
- **Offering visual comparisons** to make the financial impact crystal clear

**Perfect for:**
- 🏙️ NYC residents considering their first Citi Bike membership
- 🔄 Existing members evaluating renewal decisions
- 📊 Data-driven individuals who want accurate cost projections
- 🚴‍♀️ Anyone curious about Citi Bike's complex pricing structure

## ✨ Features

### 🎛️ Interactive Input Controls
- **Ride Frequency Slider**: Set your monthly riding patterns (0-60 rides)
- **Duration Control**: Specify average ride length (5-90 minutes)
- **E-bike Usage**: Adjust percentage of rides using electric bikes
- **Manhattan Factor**: Account for rides starting/ending in Manhattan
- **Overage Tracking**: Factor in rides that exceed time limits

### 📈 Real-Time Calculations
- **Live Updates**: Costs recalculate instantly as you adjust inputs
- **Dual Comparison**: Side-by-side member vs. non-member pricing
- **Annual Projections**: Full 12-month cost estimates
- **Savings Analysis**: Clear indication of potential savings or losses

### 📊 Visual Analytics
- **Cost Comparison Chart**: Beautiful bar chart visualization
- **Savings Metrics**: Color-coded recommendations (green=save, red=costly)
- **Personalized Insights**: Custom advice based on your riding profile

### 🎨 User Experience
- **Clean Interface**: Minimal, centered layout for easy navigation
- **Helpful Tooltips**: Contextual help for every input field
- **Mobile Responsive**: Works seamlessly on desktop and mobile devices
- **Instant Feedback**: No waiting for calculations or page reloads

## 💡 How It Works

The app uses Citi Bike's actual 2024 NYC pricing structure to provide accurate cost estimates:

### 💰 Pricing Models

**Non-Member (Pay-Per-Ride):**
- Classic bikes: $4.99 base + $0.38/min after 30 minutes
- E-bikes: $0.38/min for entire ride duration (no base fee)

**Member (Annual Subscription):**
- Annual fee: $219.99
- Classic bikes: Free for first 45 minutes, then $0.25/min
- E-bikes: $0.25/min for entire ride, with special Manhattan cap

### 🗽 Manhattan E-bike Cap Rule
For members only: E-bike rides starting or ending in Manhattan are capped at $5.00 **if and only if**:
- Ride duration ≤ 45 minutes **AND**
- Ride starts or ends in Manhattan

Otherwise, full per-minute charges apply.

## 🚀 Quick Start

1. **Clone or download** this repository
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Run the app**: `streamlit run app.py`
4. **Open browser** to `http://localhost:8501`
5. **Adjust sliders** to match your riding habits
6. **Review results** and personalized recommendations

## 📦 Installation

### Prerequisites
- **Python 3.7+** (tested with Python 3.13)
- **pip** (Python package manager)

### Step-by-Step Installation

#### Option 1: Using pip (Recommended)
```bash
# Clone the repository
git clone <repository-url>
cd citi-bike-cost-checker

# Install required packages
pip install -r requirements.txt

# Launch the application
streamlit run app.py
```

#### Option 2: Using conda
```bash
# Create a new conda environment
conda create -n citibike python=3.11
conda activate citibike

# Install packages
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

#### Option 3: Using virtual environment
```bash
# Create virtual environment
python -m venv citibike_env

# Activate virtual environment
# On Windows:
citibike_env\Scripts\activate
# On macOS/Linux:
source citibike_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch app
streamlit run app.py
```

### Required Dependencies
```
streamlit>=1.28.0
matplotlib>=3.5.0
```

## 🎮 Usage Guide

### Step 1: Set Your Riding Frequency
Use the **"How many Citi Bike rides do you take per month?"** slider to indicate your typical usage. Consider:
- Commuting patterns (work days only vs. weekends too)
- Seasonal variations (less riding in winter?)
- Occasional vs. regular usage

### Step 2: Specify Ride Duration
Adjust **"What's your average ride duration?"** based on:
- Typical trip lengths in your area
- Whether you use Citi Bike for short hops or longer journeys
- Your riding speed and route preferences

### Step 3: E-bike Preference
Set **"What percent of your rides use electric bikes?"** considering:
- Hills in your typical routes
- Personal fitness level and preferences
- Time constraints (e-bikes are faster)
- Weather conditions (e-bikes help with headwinds)

### Step 4: Manhattan Factor (E-bike users only)
If you use e-bikes, specify **"What percent of your e-bike rides start or end in Manhattan?"**:
- This affects the $5 cap benefit
- Consider your typical origins and destinations
- Manhattan includes everything below 110th Street

### Step 5: Time Limit Overages
Indicate if your rides often exceed free time limits:
- **Non-members**: 30-minute limit
- **Members**: 45-minute limit
- Consider traffic, detours, and docking availability

### Step 6: Analyze Results
Review your personalized cost analysis:
- **Green results**: Membership saves money
- **Red results**: Pay-per-ride is cheaper
- **Gray results**: Costs are roughly equal

## 🧮 Calculation Logic

### Non-Member Cost Calculation

For each ride throughout the year:

1. **Classic Bike Rides:**
   ```
   Base cost = $4.99
   If ride > 30 minutes AND user often goes over:
       Overage = (duration - 30) × $0.38 × overage_percentage
   Total = Base cost + Overage
   ```

2. **E-bike Rides:**
   ```
   Cost = Full duration × $0.38/minute
   (No base fee for e-bikes)
   ```

3. **Blended Cost:**
   ```
   Final cost = (Classic rides × Classic cost) + (E-bike rides × E-bike cost)
   ```

### Member Cost Calculation

Annual membership fee ($219.99) plus per-ride costs:

1. **Classic Bike Rides:**
   ```
   If ride > 45 minutes AND user often goes over:
       Overage = (duration - 45) × $0.25 × overage_percentage
   Else:
       Overage = $0
   ```

2. **E-bike Rides:**
   ```
   Base cost = Full duration × $0.25/minute
   
   If duration ≤ 45 minutes AND ride in Manhattan:
       Capped cost = min(Base cost, $5.00)
   Else:
       Final cost = Base cost (no cap)
   ```

### Accuracy Considerations

The app makes several assumptions for simplicity:
- **Consistent riding patterns** throughout the year
- **Average values** applied to all rides
- **Percentage-based** e-bike and overage distribution
- **2024 pricing** (rates may change annually)

## 📊 Understanding Your Results

### Cost Comparison Metrics
- **Without Membership**: Total annual cost using pay-per-ride
- **With Membership**: $219.99 + additional charges
- **Annual Savings**: Difference between the two options

### Recommendation Colors
- 🟢 **Green (Save Money)**: Membership recommended
- 🟡 **Yellow (Break Even)**: Marginal difference
- 🔴 **Red (Costs More)**: Pay-per-ride recommended

### Personalized Insights

The app provides tailored advice based on your profile:

**Light Rider (< 5 rides/month):**
- Pay-per-ride typically more economical
- Exception: Heavy e-bike usage might favor membership

**Heavy Rider (≥ 20 rides/month):**
- Membership almost always provides savings
- Benefits compound with frequency

**E-bike Enthusiast (≥ 70% e-bike usage):**
- Manhattan routes provide additional savings
- Consider route planning for maximum benefit

**Time Limit Exceeder (≥ 30% overage):**
- Consider trip planning strategies
- Break long rides into segments when possible

## 🔧 Technical Details

### Architecture
- **Framework**: Streamlit (Python web app framework)
- **Visualization**: Matplotlib for chart generation
- **Deployment**: Local development server (expandable to cloud)

### File Structure
```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This documentation file
└── .gitignore         # Git ignore patterns (if using version control)
```

### Key Functions

**`calculate_non_member_cost()`**
- Processes pay-per-ride pricing logic
- Handles classic vs. e-bike cost differences
- Applies overage charges correctly

**`calculate_member_cost()`**
- Implements membership pricing rules
- Manages Manhattan e-bike cap logic
- Calculates member-specific overages

### Performance Characteristics
- **Real-time updates**: Sub-second calculation times
- **Memory usage**: Minimal (< 50MB typical)
- **Browser compatibility**: Modern browsers (Chrome, Firefox, Safari, Edge)

## 🐛 Troubleshooting

### Common Issues

#### "ModuleNotFoundError: No module named 'matplotlib'"
**Solution**: Install missing dependencies
```bash
pip install -r requirements.txt
```

#### "streamlit: command not found"
**Solution**: Ensure Streamlit is installed and in PATH
```bash
pip install streamlit
```

#### Port Already in Use
**Solution**: Streamlit will automatically try alternative ports (8501, 8502, etc.)
```bash
# Or specify a custom port
streamlit run app.py --server.port 8503
```

#### App Won't Load in Browser
**Solutions**:
1. Check terminal for the correct URL (usually `http://localhost:8501`)
2. Try refreshing the browser page
3. Clear browser cache
4. Try an incognito/private browsing window

#### Calculations Seem Incorrect
**Verification steps**:
1. Check your input values are reasonable
2. Remember e-bike rides have no base fee for non-members
3. Manhattan cap only applies to members on rides ≤ 45 minutes
4. Overage percentages affect only a portion of your rides

### Getting Help

If you encounter issues not covered here:
1. Check the terminal output for error messages
2. Verify all dependencies are installed correctly
3. Ensure you're using a supported Python version (3.7+)
4. Try running in a fresh virtual environment

## 🤝 Contributing

### Potential Improvements
- **Historical data integration**: Import actual Citi Bike usage data
- **Seasonal adjustments**: Account for weather-based usage patterns
- **Route optimization**: Suggest cost-effective routes
- **Price updates**: Automatic fetching of current Citi Bike rates
- **Comparison tools**: Add other bike-share systems

### Development Setup
```bash
# Fork the repository
git clone <your-fork-url>
cd citi-bike-cost-checker

# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and test
streamlit run app.py

# Commit and push
git add .
git commit -m "Add your feature description"
git push origin feature/your-feature-name
```

### Code Style
- Follow PEP 8 Python style guidelines
- Add docstrings to new functions
- Include inline comments for complex logic
- Test changes thoroughly before submitting

## 📄 License

This project is open source and available under the MIT License.

### Disclaimer
This application is not affiliated with Citi Bike or Lyft. Pricing information is based on publicly available rates as of 2024 and may not reflect current pricing. Always verify current rates on the official Citi Bike website before making financial decisions.

---

**Built with ❤️ for NYC cyclists**

*Last updated: December 2024* 