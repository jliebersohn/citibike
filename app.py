import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Citi Bike Membership Cost Checker", layout="centered")

# Custom CSS for enhanced styling
st.markdown("""
<style>

    
    /* Enhanced input styling - make sliders and inputs more prominent */
    /* Clean up slider track background */
    .stSlider [data-baseweb="slider"] .st-ag {
        background: transparent !important;
    }
    
    /* Style the active portion of the slider track - Updated with better colors and refined thickness */
    .stSlider [data-baseweb="slider"] .st-an {
        background: linear-gradient(135deg, #003f7f 0%, #0056b3 100%) !important;
        height: 6px !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 6px rgba(0, 63, 127, 0.3) !important;
    }
    
    /* Target the actual slider thumb using the specific class from the HTML */
    .stSlider .st-emotion-cache-1dj3ksd,
    .stSlider [role="slider"] {
        width: 36px !important;
        height: 36px !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        border-radius: 50% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        position: relative !important;
    }
    
    /* Add bike emoji to slider handle - Made bigger and better styling */
    .stSlider .st-emotion-cache-1dj3ksd::before,
    .stSlider [role="slider"]::before {
        content: "🚲" !important;
        font-size: 36px !important;
        filter: drop-shadow(0 3px 6px rgba(0,0,0,0.4)) drop-shadow(0 0 12px rgba(0,63,127,0.2)) !important;
        position: absolute !important;
        top: 50% !important;
        left: 50% !important;
        transform: translate(-50%, -50%) !important;
        z-index: 10 !important;
    }
    
    /* Style the value display on the thumb */
    .stSlider .st-emotion-cache-b92z60 {
        font-size: 16px !important;
        font-weight: 700 !important;
        color: #003f7f !important;
        text-shadow: 0 1px 3px rgba(255,255,255,0.9) !important;
        z-index: 15 !important;
        position: relative !important;
    }
    
    /* Hover effects - just enhance the shadow, no scaling */
    .stSlider .st-emotion-cache-1dj3ksd:hover::before,
    .stSlider [role="slider"]:hover::before {
        filter: drop-shadow(0 4px 12px rgba(0,0,0,0.6)) drop-shadow(0 0 16px rgba(0,63,127,0.4)) !important;
        font-size: 36px !important;
    }
</style>

<script>
// Simple bike emoji sliders
function styleSliders() {
    const sliders = document.querySelectorAll('[role="slider"]');
    
    sliders.forEach((slider) => {
        if (!slider.hasAttribute('data-styled')) {
            slider.style.cssText += `
                width: 32px !important;
                height: 32px !important;
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
                position: relative !important;
            `;
            
            const emoji = document.createElement('div');
            emoji.innerHTML = '🚲';
            emoji.style.cssText = `
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                font-size: 24px;
                filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
                pointer-events: none;
                z-index: 999;
                font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif;
            `;
            
            slider.appendChild(emoji);
            slider.setAttribute('data-styled', 'true');
        }
    });
}

setTimeout(styleSliders, 500);
setTimeout(styleSliders, 1000);

const observer = new MutationObserver(() => setTimeout(styleSliders, 100));
observer.observe(document.body, { childList: true, subtree: true });
</script>

<style>
    
    /* Improved typography hierarchy */
    
    /* Main app title */
    h1 {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        color: #003f7f !important;
        margin-bottom: 1.5rem !important;
        line-height: 1.2 !important;
    }
    
    /* Make slider labels more prominent */
    .stSlider > label {
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        color: #003f7f !important;
        margin-bottom: 20px !important;
        line-height: 1.3 !important;
    }
    
    /* Enhanced number input styling */
    .stNumberInput > label {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        color: #003f7f !important;
        margin-bottom: 12px !important;
    }
    
    .stNumberInput > div > div > input {
        font-size: 1.3rem !important;
        padding: 14px 18px !important;
        border-radius: 12px !important;
        border: 2px solid #dee2e6 !important;
        transition: all 0.3s ease !important;
        text-align: center !important;
        font-weight: 600 !important;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #003f7f !important;
        box-shadow: 0 0 0 3px rgba(0,63,127,0.15) !important;
        transform: scale(1.02) !important;
    }

    /* Enhanced button styling */
    .stButton > button {
        border-radius: 30px !important;
        border: none !important;
        padding: 1rem 2.5rem !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 0.8px !important;
        font-size: 1.1rem !important;
        min-height: 3.5rem !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2) !important;
    }
    
    /* Color coding for bike types - Updated with better typography and reduced size */
    .classic-bike-section {
        background: linear-gradient(135deg, #17a2b8 0%, #138496 100%);
        color: white;
        padding: 12px;
        border-radius: 12px;
        margin: 8px 0;
        box-shadow: 0 4px 12px rgba(23,162,184,0.3);
    }
    
    .classic-bike-section h4 {
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        margin-bottom: 4px !important;
    }
    
    .classic-bike-section h2 {
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        margin: 6px 0 !important;
    }
    
    .classic-bike-section p {
        font-size: 0.9rem !important;
        margin: 0 !important;
    }
    
    .ebike-section {
        background: linear-gradient(135deg, #28a745 0%, #1e7e34 100%);
        color: white;
        padding: 12px;
        border-radius: 12px;
        margin: 8px 0;
        box-shadow: 0 4px 12px rgba(40,167,69,0.3);
    }
    
    .ebike-section h4 {
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        margin-bottom: 4px !important;
    }
    
    .ebike-section h2 {
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        margin: 6px 0 !important;
    }
    
    .ebike-section p {
        font-size: 0.9rem !important;
        margin: 0 !important;
    }
    
    .disabled-section {
        background: linear-gradient(135deg, #6c757d 0%, #495057 100%);
        color: white;
        padding: 24px;
        border-radius: 18px;
        margin: 12px 0;
        opacity: 0.6;
    }
    
    /* Card-based selection styling */
    .duration-card {
        background: white;
        border: 3px solid #e9ecef;
        border-radius: 18px;
        padding: 24px;
        margin: 12px 0;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .duration-card:hover {
        border-color: #003f7f;
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0,63,127,0.2);
    }
    
    .duration-card.selected {
        border-color: #003f7f;
        background: linear-gradient(135deg, #e6f0ff 0%, #cce0ff 100%);
    }
    
    /* Info box styling - Updated colors and typography */
    .info-box {
        background: linear-gradient(135deg, #e6f0ff 0%, #cce0ff 100%);
        border-left: 6px solid #003f7f;
        padding: 20px 24px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0,63,127,0.15);
        font-size: 1.1rem !important;
        line-height: 1.5 !important;
    }
    
    .info-box strong {
        font-size: 1.2rem !important;
        font-weight: 700 !important;
    }
    
    /* Step header styling - Updated colors and typography */
    .step-header {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 28px;
        border-radius: 20px;
        margin-bottom: 35px;
        border-left: 6px solid #003f7f;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    .step-header h3 {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        margin-bottom: 8px !important;
        color: #003f7f !important;
    }
    
    .step-header p {
        font-size: 1.1rem !important;
        color: #6c757d !important;
        margin: 0 !important;
    }
    

    
    /* Question styling - Enhanced typography, clean design */
    .question-label {
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        color: #003f7f !important;
        margin: 35px 0 25px 0 !important;
        line-height: 1.3 !important;
        padding: 18px 0 !important;
    }
    
    /* Improve general text readability */
    p, div {
        font-size: 1.05rem !important;
        line-height: 1.6 !important;
    }
    
    /* Results section typography */
    .st-metric-value {
        font-size: 2.5rem !important;
        font-weight: 900 !important;
    }
    
    .st-metric-label {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
    }
    
    /* Success/warning/error message improvements */
    .stSuccess, .stWarning, .stError, .stInfo {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        padding: 16px 20px !important;
        border-radius: 12px !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🗽 NYC Citi Bike Membership Calculator")

# Create tabs
tab1, tab2 = st.tabs(["💰 Cost Calculator", "📚 Pricing Guide"])

with tab1:
    st.markdown("Let's figure out if a Citi Bike membership makes financial sense for riding around the five boroughs! We'll ask a few quick questions about your NYC biking habits.")

    # Initialize session state
    if 'step' not in st.session_state:
        st.session_state.step = 1
    if 'rides_per_month' not in st.session_state:
        st.session_state.rides_per_month = 10
    if 'ebike_percentage' not in st.session_state:
        st.session_state.ebike_percentage = 50
    if 'classic_duration_dist' not in st.session_state:
        st.session_state.classic_duration_dist = {"under_20": 50, "20_40": 50, "over_40": 0}
    if 'ebike_duration_dist' not in st.session_state:
        st.session_state.ebike_duration_dist = {"under_20": 50, "20_40": 50, "over_40": 0}
    if 'manhattan_percentage' not in st.session_state:
        st.session_state.manhattan_percentage = 100
    if 'months_per_year' not in st.session_state:
        st.session_state.months_per_year = 9

    # STEP 1: Monthly rides
    if st.session_state.step == 1:
        st.markdown("""
        <div class="step-header">
            <h3 style="margin: 0; color: #003f7f;">🚲 Step 1 of 4: Your NYC Riding Frequency</h3>
            <p style="margin: 10px 0 0 0; color: #6c757d;">Tell us how often you bike around the city</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="question-label">
            How many Citi Bike rides do you take around NYC each month?
        </div>
        """, unsafe_allow_html=True)
        
        rides_per_month = st.slider(
            "",  # Empty label since we're using custom styling
            min_value=0, max_value=60, value=st.session_state.rides_per_month,
            help="Each ride is counted separately, whether classic or e‑bike.",
            label_visibility="collapsed"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="question-label">
            How many months per year do you ride?
        </div>
        """, unsafe_allow_html=True)
        
        months_per_year = st.slider(
            "",  # Empty label since we're using custom styling
            min_value=0, max_value=12, value=st.session_state.months_per_year,
            help="Most riders skip winter months due to cold weather, snow, and fewer available bikes.",
            label_visibility="collapsed",
            key="months_slider"
        )
        
        # Dynamic feedback with enhanced styling - now accounting for seasonality
        seasonal_factor = months_per_year / 12
        annual_rides = rides_per_month * 12 * seasonal_factor
        rides_per_week = annual_rides / 52
        st.markdown(f"""
        <div class="info-box">
            <strong>📊 That's about {rides_per_week:.1f} rides per week around the city</strong><br>
            <small>({annual_rides:.0f} total NYC rides per year)</small>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("✅ That looks right", type="primary"):
            st.session_state.rides_per_month = rides_per_month
            st.session_state.months_per_year = months_per_year
            st.session_state.step = 2
            st.rerun()

    # STEP 2: E-bike percentage
    elif st.session_state.step == 2:
        st.markdown("""
        <div class="step-header">
            <h3 style="margin: 0; color: #003f7f;">⚡ Step 2 of 4: E-Bike vs Classic</h3>
            <p style="margin: 10px 0 0 0; color: #6c757d;">NYC e-bikes cost more but get you there faster!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="question-label">
            What percentage of your NYC rides use electric bikes?
        </div>
        """, unsafe_allow_html=True)
        
        ebike_percentage = st.slider(
            "",  # Empty label since we're using custom styling
            min_value=0, max_value=100, value=st.session_state.ebike_percentage,
            help="E-bikes cost more per minute but are faster and easier to ride.",
            label_visibility="collapsed",
            format="%d%%"
        )
        
        # Dynamic feedback with color coding - account for seasonality
        seasonal_factor = st.session_state.months_per_year / 12
        annual_rides = st.session_state.rides_per_month * 12 * seasonal_factor
        total_rides_per_week = annual_rides / 52
        ebike_rides = total_rides_per_week * (ebike_percentage / 100)
        classic_rides = total_rides_per_week * (1 - ebike_percentage / 100)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="classic-bike-section" style="text-align: center;">
                <h4 style="margin: 0;">🚲 Classic Bikes</h4>
                <h2 style="margin: 10px 0;">{classic_rides:.1f}</h2>
                <p style="margin: 0;">rides per week</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="ebike-section" style="text-align: center;">
                <h4 style="margin: 0;">⚡ E-Bikes</h4>
                <h2 style="margin: 10px 0;">{ebike_rides:.1f}</h2>
                <p style="margin: 0;">rides per week</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Navigation buttons
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("← Back", type="secondary"):
                st.session_state.step = 1
                st.rerun()
        with col2:
            if st.button("✅ Looks good", type="primary"):
                st.session_state.ebike_percentage = ebike_percentage
                st.session_state.step = 3
                st.rerun()

    # Duration mapping for buckets
    duration_map = {"under_20": 15, "20_40": 30, "over_40": 55}

    # CALCULATION FUNCTIONS
    def calculate_cost_for_duration_bucket(duration, bike_type, is_member=False, manhattan_ratio=0, overage_ratio=0.2):
        """Calculate cost for a single ride of given duration and bike type."""
        if is_member:
            # Member pricing
            if bike_type == "classic":
                if duration <= 45:
                    return 0  # Free for members
                else:
                    return (duration - 45) * 0.25 * overage_ratio
            else:  # e-bike
                base_cost = duration * 0.25
                # Apply Manhattan cap if applicable
                if duration <= 45 and manhattan_ratio > 0:
                    capped_cost = min(base_cost, 5.00)
                    return (manhattan_ratio * capped_cost) + ((1 - manhattan_ratio) * base_cost)
                else:
                    return base_cost
        else:
            # Non-member pricing
            if bike_type == "classic":
                base_cost = 4.99
                if duration > 30:
                    base_cost += (duration - 30) * 0.38 * overage_ratio
                return base_cost
            else:  # e-bike
                return duration * 0.38  # No base fee for e-bikes

    def calculate_costs(rides_per_month, ebike_percentage, classic_duration_dist, ebike_duration_dist, manhattan_percentage, months_per_year, overage_percent=20):
        """Calculate both member and non-member costs."""
        membership_fee = 219.99
        seasonal_factor = months_per_year / 12
        rides_per_year = rides_per_month * 12 * seasonal_factor
        ebike_ratio = ebike_percentage / 100
        manhattan_ratio = manhattan_percentage / 100
        overage_ratio = overage_percent / 100
        
        non_member_cost = 0
        member_cost = membership_fee
        classic_ride_ratio = 1 - ebike_ratio
        
        for _ in range(int(rides_per_year)):
            non_member_ride_cost = 0
            member_ride_cost = 0
            
            # Classic bike rides
            if classic_ride_ratio > 0:
                for bucket, percentage in classic_duration_dist.items():
                    duration = duration_map[bucket]
                    non_member_bucket_cost = calculate_cost_for_duration_bucket(duration, "classic", False, manhattan_ratio, overage_ratio)
                    member_bucket_cost = calculate_cost_for_duration_bucket(duration, "classic", True, manhattan_ratio, overage_ratio)
                    
                    non_member_ride_cost += classic_ride_ratio * (percentage / 100) * non_member_bucket_cost
                    member_ride_cost += classic_ride_ratio * (percentage / 100) * member_bucket_cost
            
            # E-bike rides
            if ebike_ratio > 0:
                for bucket, percentage in ebike_duration_dist.items():
                    duration = duration_map[bucket]
                    non_member_bucket_cost = calculate_cost_for_duration_bucket(duration, "ebike", False, manhattan_ratio, overage_ratio)
                    member_bucket_cost = calculate_cost_for_duration_bucket(duration, "ebike", True, manhattan_ratio, overage_ratio)
                    
                    non_member_ride_cost += ebike_ratio * (percentage / 100) * non_member_bucket_cost
                    member_ride_cost += ebike_ratio * (percentage / 100) * member_bucket_cost
            
            non_member_cost += non_member_ride_cost
            member_cost += member_ride_cost
        
        return member_cost, non_member_cost

    def calculate_breakeven_rides(ebike_percentage, classic_duration_dist, ebike_duration_dist, manhattan_percentage, months_per_year, overage_percent=20):
        """Calculate the number of monthly rides where member and non-member costs are equal."""
        # Try different ride counts to find breakeven point
        for rides in range(1, 100):
            member_cost, non_member_cost = calculate_costs(rides, ebike_percentage, classic_duration_dist, ebike_duration_dist, manhattan_percentage, months_per_year, overage_percent)
            if member_cost <= non_member_cost:
                return rides
        return float('inf')  # Never breaks even

    # STEP 3: Duration breakdowns
    if st.session_state.step == 3:
        st.markdown("""
        <div class="step-header">
            <h3 style="margin: 0; color: #003f7f;">⏱️ Step 3 of 4: Your NYC Trip Times</h3>
            <p style="margin: 10px 0 0 0; color: #6c757d;">Short trips around the block or longer rides across boroughs?</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        # Classic bike durations
        with col1:
            if st.session_state.ebike_percentage < 100:
                st.markdown("""
                <div class="classic-bike-section">
                    <h4 style="margin: 0 0 15px 0; text-align: center;">🚲 Classic Bike Rides</h4>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("**% of classic rides under 20 minutes**")
                classic_under_20 = st.slider(
                    "",  # Empty label since we're using custom styling
                    min_value=0, max_value=100, value=st.session_state.classic_duration_dist["under_20"],
                    key="classic_under_20", label_visibility="collapsed", format="%d%%"
                )
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                
                st.markdown("**% of classic rides 20-40 minutes**")
                classic_20_40 = st.slider(
                    "",  # Empty label since we're using custom styling
                    min_value=0, max_value=100, value=st.session_state.classic_duration_dist["20_40"],
                    key="classic_20_40", label_visibility="collapsed", format="%d%%"
                )
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                
                st.markdown("**% of classic rides over 40 minutes**")
                classic_over_40 = st.slider(
                    "",  # Empty label since we're using custom styling
                    min_value=0, max_value=100, value=st.session_state.classic_duration_dist["over_40"],
                    key="classic_over_40", label_visibility="collapsed", format="%d%%"
                )
                
                classic_total = classic_under_20 + classic_20_40 + classic_over_40
                
                # Show progress bar for classic bikes
                if classic_total == 100:
                    st.success("✅ Perfect! Totals 100%")
                else:
                    st.warning(f"⚠️ Currently {classic_total}% (need 100%)")
                
                classic_duration_dist = {"under_20": classic_under_20, "20_40": classic_20_40, "over_40": classic_over_40}
            else:
                st.markdown("""
                <div class="disabled-section">
                    <h4 style="margin: 0 0 15px 0; text-align: center;">🚲 Classic Bike Rides</h4>
                    <p style="margin: 0; text-align: center; opacity: 0.8;">Not applicable - you selected 100% e-bike usage</p>
                </div>
                """, unsafe_allow_html=True)
                classic_duration_dist = {"under_20": 50, "20_40": 50, "over_40": 0}  # Default values
        
        # E-bike durations
        with col2:
            if st.session_state.ebike_percentage > 0:
                st.markdown("""
                <div class="ebike-section">
                    <h4 style="margin: 0 0 15px 0; text-align: center;">⚡ Electric Bike Rides</h4>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("**% of e-bike rides under 20 minutes**")
                ebike_under_20 = st.slider(
                    "",  # Empty label since we're using custom styling
                    min_value=0, max_value=100, value=st.session_state.ebike_duration_dist["under_20"],
                    key="ebike_under_20", label_visibility="collapsed", format="%d%%"
                )
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                
                st.markdown("**% of e-bike rides 20-40 minutes**")
                ebike_20_40 = st.slider(
                    "",  # Empty label since we're using custom styling
                    min_value=0, max_value=100, value=st.session_state.ebike_duration_dist["20_40"],
                    key="ebike_20_40", label_visibility="collapsed", format="%d%%"
                )
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                
                st.markdown("**% of e-bike rides over 40 minutes**")
                ebike_over_40 = st.slider(
                    "",  # Empty label since we're using custom styling
                    min_value=0, max_value=100, value=st.session_state.ebike_duration_dist["over_40"],
                    key="ebike_over_40", label_visibility="collapsed", format="%d%%"
                )
                
                ebike_total = ebike_under_20 + ebike_20_40 + ebike_over_40
                
                # Show progress bar for e-bikes
                if ebike_total == 100:
                    st.success("✅ Perfect! Totals 100%")
                else:
                    st.warning(f"⚠️ Currently {ebike_total}% (need 100%)")
                
                ebike_duration_dist = {"under_20": ebike_under_20, "20_40": ebike_20_40, "over_40": ebike_over_40}
            else:
                st.markdown("""
                <div class="disabled-section">
                    <h4 style="margin: 0 0 15px 0; text-align: center;">⚡ Electric Bike Rides</h4>
                    <p style="margin: 0; text-align: center; opacity: 0.8;">Not applicable - you selected 0% e-bike usage</p>
                </div>
                """, unsafe_allow_html=True)
                ebike_duration_dist = {"under_20": 50, "20_40": 50, "over_40": 0}  # Default values
        
        # Validation and confirmation
        valid = True
        if st.session_state.ebike_percentage < 100:
            if classic_total != 100:
                valid = False
        if st.session_state.ebike_percentage > 0:
            if ebike_total != 100:
                valid = False
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Navigation buttons
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("← Back", type="secondary"):
                st.session_state.step = 2
                st.rerun()
        with col2:
            if valid:
                if st.button("✅ All set", type="primary"):
                    st.session_state.classic_duration_dist = classic_duration_dist
                    st.session_state.ebike_duration_dist = ebike_duration_dist
                    st.session_state.step = 4
                    st.rerun()
            else:
                st.button("✅ All set", type="primary", disabled=True)
        
        if not valid:
            st.error("💡 Tip: Make sure all percentages add up to exactly 100% before continuing.")

    # STEP 4: Manhattan percentage
    elif st.session_state.step == 4:
        st.markdown("""
        <div class="step-header">
            <h3 style="margin: 0; color: #003f7f;">🗽 Step 4 of 4: Manhattan vs The Outer Boroughs</h3>
            <p style="margin: 10px 0 0 0; color: #6c757d;">E-bike pricing is capped in Manhattan - this affects your savings!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="question-label">
            What percentage of your rides are in Manhattan vs. the other 4 boroughs?
        </div>
        """, unsafe_allow_html=True)
        
        manhattan_percentage = st.slider(
            "",  # Empty label since we're using custom styling
            min_value=0, max_value=100, value=st.session_state.manhattan_percentage,
            help="Include rides that start, end, or pass through Manhattan (vs. Brooklyn, Queens, Bronx, Staten Island). E-bike rides in Manhattan have a $5 cap that can save you money!",
            label_visibility="collapsed",
            format="%d%%"
        )
        
        # Enhanced feedback for Manhattan usage
        if manhattan_percentage > 0:
            st.markdown(f"""
            <div class="info-box">
                <strong>🗽 {manhattan_percentage}% of your rides are in the heart of NYC!</strong><br>
                <small>These rides benefit from the Manhattan e-bike $5 cap</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="info-box">
                <strong>🌉 All rides in Brooklyn, Queens, Bronx & Staten Island</strong><br>
                <small>Your e-bike rides won't benefit from the Manhattan $5 cap, but that's perfectly fine!</small>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Navigation buttons
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("← Back", type="secondary"):
                st.session_state.step = 3
                st.rerun()
        with col2:
            if st.button("▶️ Show Cost Analysis", type="primary"):
                st.session_state.manhattan_percentage = manhattan_percentage
                st.session_state.step = 5
                st.rerun()

    # STEP 5: Results
    elif st.session_state.step == 5:
        # Set variables for calculations
        rides_per_month = st.session_state.rides_per_month
        ebike_percentage = st.session_state.ebike_percentage
        classic_duration_dist = st.session_state.classic_duration_dist
        ebike_duration_dist = st.session_state.ebike_duration_dist
        manhattan_percentage = st.session_state.manhattan_percentage
        months_per_year = st.session_state.months_per_year
        
        # Fixed settings for simplified flow
        overage_percent = 20  # Default assumption
        show_monthly = False  # Default to annual view

        # Calculate costs
        member_cost, non_member_cost = calculate_costs(
            rides_per_month, ebike_percentage, classic_duration_dist, 
            ebike_duration_dist, manhattan_percentage, months_per_year, overage_percent
        )
        
        savings = non_member_cost - member_cost
        
        # Calculate breakeven point
        breakeven_rides = calculate_breakeven_rides(
            ebike_percentage, classic_duration_dist, ebike_duration_dist, manhattan_percentage, months_per_year, overage_percent
        )
        
        st.markdown("""
        <div class="step-header">
            <h2 style="margin: 0; color: #003f7f;">📊 Your NYC Biking Cost Analysis</h2>
            <p style="margin: 10px 0 0 0; color: #6c757d;">Here's your personalized analysis for biking around the Big Apple!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Initialize session state for date if not exists
        if 'analysis_date' not in st.session_state:
            from datetime import datetime
            st.session_state.analysis_date = datetime.now().strftime("%Y-%m-%d")
        
        # Display results
        display_member_cost = member_cost / 12 if show_monthly else member_cost
        display_non_member_cost = non_member_cost / 12 if show_monthly else non_member_cost
        display_savings = savings / 12 if show_monthly else savings
        period_label = "Monthly" if show_monthly else "Annual"
        period_text = "month" if show_monthly else "year"

        st.markdown(f"### 📊 Your Estimated {period_label} Costs")

        col1, col2 = st.columns(2)
        col1.metric("Without Membership", f"${display_non_member_cost:,.2f}")
        col2.metric("With Membership", f"${display_member_cost:,.2f}")

        if display_savings > 0:
            st.success(f"🗽 You're ready to bike the Big Apple! You'll save **${display_savings:,.2f} per {period_text}** with a Citi Bike membership.")
        elif display_savings < 0:
            st.warning(f"🚫 A Citi Bike membership would cost you **${-display_savings:,.2f} more per {period_text}**.")
        else:
            st.info("😐 You're breaking even with or without a membership.")

        # Breakeven analysis
        if breakeven_rides != float('inf'):
            if breakeven_rides < rides_per_month:
                st.info(f"💡 With your settings, a Citi Bike membership breaks even at approximately **{breakeven_rides} rides per month**. You're currently above this threshold!")
            else:
                st.info(f"💡 With your settings, a Citi Bike membership breaks even at approximately **{breakeven_rides} rides per month**. You would need to ride more to benefit from membership.")
        else:
            st.info("💡 Based on your riding pattern, pay-per-ride is consistently more economical than membership.")

        # Bar Chart Comparison
        st.markdown(f"### 📈 {period_label} Cost Comparison")
        
        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.bar(["Without Membership", "With Membership"], [display_non_member_cost, display_member_cost], 
                      color=['#ff6b6b', '#4ecdc4'])
        ax.set_ylabel(f"Total {period_label} Cost ($)")
        ax.set_title(f"{period_label} Citi Bike Costs Comparison")
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + (height * 0.02),
                    f'${height:,.0f}', ha='center', va='bottom')
        
        # Improve styling
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='y', alpha=0.3)
        
        st.pyplot(fig)

        # Additional insights
        st.markdown("### 💭 Additional Insights")
        
        if rides_per_month < 5:
            st.info("💡 **Light rider**: With fewer than 5 rides per month, pay-per-ride might be more economical unless you use e-bikes frequently.")
        elif rides_per_month >= 20:
            st.info("💡 **Heavy rider**: With 20+ rides per month, a membership typically provides significant savings.")
        
        if ebike_percentage >= 70:
            st.info("⚡ **E-bike lover**: Since you use e-bikes frequently, consider routes in Manhattan for the $5 cap benefit.")
        
        # Summary Output Section
        st.markdown("### 📤 Your Analysis Summary")
        
        def generate_summary_text(member_cost, non_member_cost, show_monthly=False):
            """Generate a copyable summary of the cost analysis."""
            period = "month" if show_monthly else "year"
            
            if show_monthly:
                member_cost = member_cost / 12
                non_member_cost = non_member_cost / 12
            
            ebike_text = f", with {ebike_percentage}% e-bike usage" if ebike_percentage > 0 else ""
            seasonal_text = f" over {st.session_state.months_per_year} active months" if st.session_state.months_per_year < 12 else ""
            duration_text = " with varied ride durations"
            
            savings = non_member_cost - member_cost
            
            if savings > 0:
                recommendation = f"A Citi Bike membership would save you ${savings:.2f} per {period}."
            elif savings < 0:
                recommendation = f"Pay-per-ride would save you ${abs(savings):.2f} per {period} compared to membership."
            else:
                recommendation = f"Both options cost about the same (${member_cost:.2f} per {period})."
            
            summary = f"""🗽 NYC CITI BIKE COST ANALYSIS SUMMARY

🚴 Riding Pattern: {rides_per_month} rides per month around NYC{seasonal_text}{ebike_text}{duration_text}

💰 Cost Comparison:
• With Membership: ${member_cost:.2f} per {period}
• Without Membership: ${non_member_cost:.2f} per {period}

💡 Recommendation: {recommendation}

Generated on {st.session_state.get('analysis_date', 'today')} using 2024 Citi Bike NYC pricing."""
            
            return summary
        
        summary_text = generate_summary_text(member_cost, non_member_cost, show_monthly)
        
        # Display the summary in a text area for easy copying
        st.text_area(
            "Copy your personalized cost analysis:",
            value=summary_text,
            height=200,
            help="Select all text (Ctrl+A) and copy (Ctrl+C) to share or save your analysis"
        )
        
        # Download button
        st.download_button(
            label="📥 Download Summary as Text File",
            data=summary_text,
            file_name=f"citibike_analysis_{st.session_state.analysis_date}.txt",
            mime="text/plain",
            help="Download your cost analysis as a text file"
        )
        
        # Navigation buttons
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("← Back to Edit", type="secondary"):
                st.session_state.step = 4
                st.rerun()
        with col2:
            if st.button("🔄 Start Over", type="secondary"):
                st.session_state.step = 1
                st.rerun()

    # Footer
    st.markdown("---")
    st.markdown("*Pricing based on Citi Bike NYC rates as of 2024. Actual costs may vary.*")

# Add the new tab for pricing guide
with tab2:
    st.markdown("### 🗽 How NYC Citi Bike Pricing Works")
    st.markdown("Your comprehensive guide to understanding membership vs. pay-per-ride costs in the five boroughs.")
    
    # Create subtabs for different sections
    subtab1, subtab2, subtab3, subtab4 = st.tabs(["🚴 Membership Plans", "⚡ E-Bike Pricing", "📍 Location Rules", "💡 Quick Examples"])
    
    with subtab1:
        st.markdown("## 🚴 Membership Plans")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 💰 Pay-Per-Ride (No Membership)
            
            **Classic Bikes:**
            - 🚲 **$4.99** base fare per ride
            - 🕐 **30 minutes** included with base fare
            - ⏰ **$0.38/minute** for every minute over 30 minutes
            
            **E-Bikes:**
            - ⚡ **No base fare** - pay only for time used
            - ⏰ **$0.38/minute** for the entire ride
            """)
            
        with col2:
            st.markdown("""
            ### 🎫 Annual Membership ($219.99/year)
            
            **Classic Bikes:**
            - 🚲 **FREE** for rides up to 45 minutes
            - ⏰ **$0.25/minute** for every minute over 45 minutes
            
            **E-Bikes:**
            - ⚡ **$0.25/minute** for the entire ride
            - 🗽 **$5 cap** in Manhattan (if ≤45 minutes)
            """)
        
        st.info("💡 **Key Insight**: Members get 15 extra free minutes on classic bikes (45 vs 30) and pay less per minute on all overage time.")
    
    with subtab2:
        st.markdown("## ⚡ E-Bike Pricing Deep Dive")
        
        st.markdown("### Why E-Bikes Cost More")
        st.markdown("""
        - **Faster**: Average 20% quicker than classic bikes
        - **Less effort**: Electric assist makes hills and long distances easier
        - **Higher maintenance**: Batteries, motors, and electronics need more upkeep
        - **Popular**: High demand means premium pricing
        """)
        
        st.markdown("### E-Bike Cost Comparison")
        
        # E-bike comparison table
        import pandas as pd
        ebike_data = {
            'Ride Duration': ['15 minutes', '30 minutes', '45 minutes', '60 minutes'],
            'Pay-Per-Ride': ['$5.70', '$11.40', '$17.10', '$22.80'],
            'Member (Non-Manhattan)': ['$3.75', '$7.50', '$11.25', '$15.00'],
            'Member (Manhattan)': ['$3.75', '$5.00*', '$5.00*', '$15.00']
        }
        df_ebike = pd.DataFrame(ebike_data)
        st.dataframe(df_ebike, use_container_width=True)
        st.caption("*Manhattan cap applies only to rides ≤45 minutes")
        
        st.warning("🗽 **Manhattan E-Bike Cap**: Members pay maximum $5 for e-bike rides in Manhattan that are 45 minutes or less. This is a significant savings opportunity!")
    
    with subtab3:
        st.markdown("## 📍 Location-Based Pricing Rules")
        
        st.markdown("### Manhattan vs. Other Boroughs")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🗽 Manhattan
            - **E-bike cap**: $5 maximum for members (≤45 min rides)
            - **High density**: More docking stations
            - **Business district**: Premium pricing justified
            """)
            
        with col2:
            st.markdown("""
            ### 🌉 Brooklyn, Queens, Bronx, Staten Island
            - **No special caps**: Standard per-minute pricing
            - **Growing network**: Rapidly expanding coverage
            - **Standard rates**: Same pricing as rest of system
            """)
        
        st.markdown("### How the Manhattan Cap Works")
        st.markdown("""
        The Manhattan e-bike cap is **only for members** and applies when:
        1. ✅ You have an annual membership
        2. ✅ The ride is 45 minutes or less
        3. ✅ The ride starts, ends, or passes through Manhattan
        
        **Example**: A 30-minute Manhattan e-bike ride costs:
        - 💰 Pay-per-ride: $11.40 (30 × $0.38)
        - 🎫 Member: $5.00 (capped)
        - 🎉 Savings: $6.40 per ride
        """)
    
    with subtab4:
        st.markdown("## 💡 Real NYC Scenarios")
        
        st.markdown("### Scenario 1: The Commuter")
        st.info("""
        **Profile**: 40 rides/month, 70% e-bike, mostly 25-minute rides, 80% in Manhattan, 10 active months
        
        **Annual Costs**:
        - Pay-per-ride: ~$3,420
        - Membership: ~$1,080
        - **Savings with membership**: ~$2,340/year
        
        **Verdict**: Membership is a no-brainer! 💪
        """)
        
        st.markdown("### Scenario 2: The Weekend Explorer")
        st.info("""
        **Profile**: 6 rides/month, 40% e-bike, mix of 20-45 minute rides, 50% in Manhattan, 8 active months
        
        **Annual Costs**:
        - Pay-per-ride: ~$480
        - Membership: ~$380
        - **Savings with membership**: ~$100/year
        
        **Verdict**: Membership still saves money, but less dramatically 📊
        """)
        
        st.markdown("### Scenario 3: The Occasional User")
        st.warning("""
        **Profile**: 3 rides/month, 20% e-bike, mostly short 15-minute rides, 30% in Manhattan, 6 active months
        
        **Annual Costs**:
        - Pay-per-ride: ~$200
        - Membership: ~$290
        - **Extra cost with membership**: ~$90/year
        
        **Verdict**: Pay-per-ride is better for light usage 🚲
        """)
        
        st.markdown("### Quick Decision Framework")
        st.success("""
        **Get the membership if you:**
        - Take 8+ rides per month
        - Use e-bikes frequently
        - Ride in Manhattan often
        - Are active 6+ months per year
        
        **Pay-per-ride if you:**
        - Take fewer than 5 rides per month
        - Rarely use e-bikes
        - Ride mostly in outer boroughs
        - Are a very occasional user
        """)
        
        st.markdown("### Break-Even Analysis")
        st.markdown("""
        **Typical break-even points**:
        - Heavy e-bike users (70%+): ~4-6 rides/month
        - Mixed users (50% e-bike): ~8-12 rides/month  
        - Classic bike only: ~15-20 rides/month
        - Light users (<20% e-bike): ~20-25 rides/month
        
        *Assumes typical NYC riding patterns and seasonality*
        """)
    
    st.markdown("---")
    st.markdown("### 🔗 Official Resources")
    st.markdown("""
    - [Citi Bike Official Pricing](https://citibikenyc.com/pricing)
    - [System Map](https://citibikenyc.com/system-data)
    - [Member Benefits](https://citibikenyc.com/how-it-works)
    """)
    
    st.caption("*All pricing information based on NYC Citi Bike rates as of 2024. Rates subject to change.*") 