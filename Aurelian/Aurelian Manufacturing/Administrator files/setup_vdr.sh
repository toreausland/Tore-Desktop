#!/bin/bash
# ============================================================================
# AURELIAN MANUFACTURING — Virtual Data Room (VDR) Setup
# ============================================================================
# Professional investor-grade folder structure
# Covers: Pre-Seed → Seed → Series A
# Standard: Aligned with Nordic VC / European institutional DD expectations
# ============================================================================

VDR_ROOT="${1:-.}/Aurelian_VDR"

echo "🏗️  Creating Aurelian Manufacturing VDR structure..."
echo "    Location: $VDR_ROOT"
echo ""

# ============================================================================
# 00 — EXECUTIVE SUMMARY (First thing investors open)
# ============================================================================
mkdir -p "$VDR_ROOT/00_Executive_Summary"

# ============================================================================
# 01 — CORPORATE & GOVERNANCE
# ============================================================================
mkdir -p "$VDR_ROOT/01_Corporate_Governance/1.1_Formation_Documents"
mkdir -p "$VDR_ROOT/01_Corporate_Governance/1.2_Shareholder_Agreements"
mkdir -p "$VDR_ROOT/01_Corporate_Governance/1.3_Board_Governance"
mkdir -p "$VDR_ROOT/01_Corporate_Governance/1.3_Board_Governance/Board_Minutes"
mkdir -p "$VDR_ROOT/01_Corporate_Governance/1.4_Cap_Table"
mkdir -p "$VDR_ROOT/01_Corporate_Governance/1.5_Organizational_Structure"
mkdir -p "$VDR_ROOT/01_Corporate_Governance/1.6_Founder_Vesting"

# ============================================================================
# 02 — FINANCIAL
# ============================================================================
mkdir -p "$VDR_ROOT/02_Financial/2.1_Financial_Model"
mkdir -p "$VDR_ROOT/02_Financial/2.2_Financing_Plan"
mkdir -p "$VDR_ROOT/02_Financial/2.3_Valuation_Basis"
mkdir -p "$VDR_ROOT/02_Financial/2.4_Economic_Tables_Projections"
mkdir -p "$VDR_ROOT/02_Financial/2.5_Sensitivity_Analysis"
mkdir -p "$VDR_ROOT/02_Financial/2.6_Use_of_Funds"
mkdir -p "$VDR_ROOT/02_Financial/2.7_VC_Benchmarks_Comparables"
mkdir -p "$VDR_ROOT/02_Financial/2.8_Tax_Accounting"

# ============================================================================
# 03 — COMMERCIAL & MARKET
# ============================================================================
mkdir -p "$VDR_ROOT/03_Commercial_Market/3.1_Market_Analysis"
mkdir -p "$VDR_ROOT/03_Commercial_Market/3.1_Market_Analysis/Defence"
mkdir -p "$VDR_ROOT/03_Commercial_Market/3.1_Market_Analysis/Energy"
mkdir -p "$VDR_ROOT/03_Commercial_Market/3.1_Market_Analysis/Critical_Infrastructure"
mkdir -p "$VDR_ROOT/03_Commercial_Market/3.2_Competitive_Landscape"
mkdir -p "$VDR_ROOT/03_Commercial_Market/3.3_Customer_Pipeline"
mkdir -p "$VDR_ROOT/03_Commercial_Market/3.3_Customer_Pipeline/LOIs_MOUs"
mkdir -p "$VDR_ROOT/03_Commercial_Market/3.3_Customer_Pipeline/Discovery_Notes"
mkdir -p "$VDR_ROOT/03_Commercial_Market/3.4_Go_To_Market_Strategy"
mkdir -p "$VDR_ROOT/03_Commercial_Market/3.5_Pricing_Revenue_Model"
mkdir -p "$VDR_ROOT/03_Commercial_Market/3.6_Market_Trends_Projections"

# ============================================================================
# 04 — TECHNICAL & OPERATIONS
# ============================================================================
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.1_Technology_Overview"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.2_CNC_Equipment"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.2_CNC_Equipment/Specifications"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.2_CNC_Equipment/Resale_Value_Analysis"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.2_CNC_Equipment/Supplier_Agreements"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.3_Automation_Validation"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.4_Facility_Real_Estate"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.4_Facility_Real_Estate/Lease_Agreements"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.4_Facility_Real_Estate/Architectural_Plans"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.5_Quality_Certifications"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.5_Quality_Certifications/ISO_Roadmap"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.5_Quality_Certifications/AQAP_Defence"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.6_Production_Timeline"
mkdir -p "$VDR_ROOT/04_Technical_Operations/4.7_Risk_Register"

# ============================================================================
# 05 — LEGAL & IP
# ============================================================================
mkdir -p "$VDR_ROOT/05_Legal_IP/5.1_IP_Ownership"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.1_IP_Ownership/Patents_Trademarks"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.1_IP_Ownership/IP_Assignment_Agreements"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.2_Material_Contracts"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.2_Material_Contracts/Employment_Agreements"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.2_Material_Contracts/Advisory_Agreements"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.2_Material_Contracts/Supplier_Contracts"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.2_Material_Contracts/Customer_Contracts"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.3_Regulatory_Compliance"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.3_Regulatory_Compliance/Export_Control"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.3_Regulatory_Compliance/Environmental"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.4_Insurance"
mkdir -p "$VDR_ROOT/05_Legal_IP/5.5_Permits_Licenses"

# ============================================================================
# 06 — TEAM & PEOPLE
# ============================================================================
mkdir -p "$VDR_ROOT/06_Team/6.1_Founders"
mkdir -p "$VDR_ROOT/06_Team/6.1_Founders/CVs"
mkdir -p "$VDR_ROOT/06_Team/6.1_Founders/References"
mkdir -p "$VDR_ROOT/06_Team/6.2_Board_of_Directors"
mkdir -p "$VDR_ROOT/06_Team/6.3_Advisors"
mkdir -p "$VDR_ROOT/06_Team/6.3_Advisors/Bios"
mkdir -p "$VDR_ROOT/06_Team/6.3_Advisors/Advisory_Agreements"
mkdir -p "$VDR_ROOT/06_Team/6.4_Key_Hires_Plan"
mkdir -p "$VDR_ROOT/06_Team/6.5_ESOP_Option_Pool"

# ============================================================================
# 07 — PRESENTATIONS & PITCH MATERIALS
# ============================================================================
mkdir -p "$VDR_ROOT/07_Presentations/7.1_Investor_Pitch_Deck"
mkdir -p "$VDR_ROOT/07_Presentations/7.2_One_Pagers"
mkdir -p "$VDR_ROOT/07_Presentations/7.3_Video_Pitch"
mkdir -p "$VDR_ROOT/07_Presentations/7.4_Press_Media"

# ============================================================================
# 08 — DD PROCESS (Internal — not shared with investors)
# ============================================================================
mkdir -p "$VDR_ROOT/08_DD_Process_Internal/8.1_Checklists"
mkdir -p "$VDR_ROOT/08_DD_Process_Internal/8.2_QA_Database"
mkdir -p "$VDR_ROOT/08_DD_Process_Internal/8.3_Investor_Tracking"
mkdir -p "$VDR_ROOT/08_DD_Process_Internal/8.4_Gap_Analysis"
mkdir -p "$VDR_ROOT/08_DD_Process_Internal/8.5_Response_Templates"
mkdir -p "$VDR_ROOT/08_DD_Process_Internal/8.6_Meeting_Notes"

# ============================================================================
# 09 — APPENDICES (Vedlegg / Supporting Evidence)
# ============================================================================
mkdir -p "$VDR_ROOT/09_Appendices/Vedlegg_A_Investment_Memo"
mkdir -p "$VDR_ROOT/09_Appendices/Vedlegg_B_Economic_Tables"
mkdir -p "$VDR_ROOT/09_Appendices/Vedlegg_C_Industrial_Benchmarks"
mkdir -p "$VDR_ROOT/09_Appendices/Vedlegg_D_Automation_Validation"
mkdir -p "$VDR_ROOT/09_Appendices/Vedlegg_E_CNC_Resale_Value"
mkdir -p "$VDR_ROOT/09_Appendices/Vedlegg_F_Team_Governance"
mkdir -p "$VDR_ROOT/09_Appendices/Vedlegg_G_Facility_Strategy"
mkdir -p "$VDR_ROOT/09_Appendices/Additional_Research"

echo "✅ VDR structure created successfully!"
echo ""

# Count folders
FOLDER_COUNT=$(find "$VDR_ROOT" -type d | wc -l)
echo "📁 Total folders: $FOLDER_COUNT"
echo ""

# Print tree
echo "📂 FOLDER STRUCTURE:"
echo "============================================================================"
find "$VDR_ROOT" -type d | sort | sed "s|$VDR_ROOT|Aurelian_VDR|" | \
  awk '{
    n = split($0, parts, "/")
    indent = ""
    for (i = 1; i < n; i++) indent = indent "    "
    if (n == 1) print $0 "/"
    else print indent "├── " parts[n] "/"
  }'
echo "============================================================================"
echo ""
echo "🚀 Next: Run the document placement guide to see where each file goes."
