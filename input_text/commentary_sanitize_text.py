import re

# Dictionary of flagged terms and neutral replacements
flagged_terms = {
    # Legal risk
    "lawsuit": "legal dispute",
    "sued": "involved in legal proceedings",
    "sue": "pursue legal remedy",
    "settlement": "resolution",
    "illegal": "non-compliant",
    "fraud": "financial misconduct",
    "fraudulent": "potentially misleading",
    "discrimination": "biased practices",
    "harassment": "workplace misconduct",
    "hostile work environment": "challenging workplace climate",

    # Antitrust / competition
    "monopoly": "market dominance",
    "anti-competitive": "limiting market flexibility",
    "price fixing": "coordinated pricing",
    "collusion": "non-competitive behavior",

    # Insider/financial concerns
    "insider trading": "internal misuse of information",
    "embezzlement": "financial misappropriation",
    "kickback": "improper compensation",
    "bribery": "unethical incentive",
    "audit failure": "audit concerns",
    "restatement": "revised financials",

    # Performance / HR
    "fired": "let go",
    "terminated": "role ended",
    "layoff": "reduction in force",
    "poor performance": "underperformance",
    "incompetent": "underqualified",
    "negligent": "lacking due diligence",

    # Ethics / reputation
    "corrupt": "ethically questionable",
    "unethical": "against policy",
    "toxic": "non-collaborative",
    "retaliation": "adverse response",
    "whistleblower": "internal reporter",

    # Finance sensitivities
    "bankrupt": "financially distressed",
    "insolvent": "liquidity-constrained",
    "default": "payment delay",
    "off the books": "non-standard reporting",
    "cooked the books": "manipulated accounting",
    "shell company": "intermediary entity",
    "laundering": "misuse of financial flow",

    # Compliance
    "non-compliant": "lacking full adherence",
    "violation": "compliance issue",
    "breach": "policy deviation",
    "penalty": "regulatory consequence",
    "fine": "regulatory charge",
    "sanction": "external restriction",

    # Sensitive operational terms
    "shutdown": "temporary pause in operations",
    "failure": "underperformance",
    "collapse": "rapid decline",
    "crisis": "challenging period",
    "cover-up": "internal miscommunication",
    "leak": "unintended disclosure"
}


def sanitize_text(text):
    sanitized = text
    for term, replacement in flagged_terms.items():
        # Use regex for whole-word replacement, case-insensitive
        pattern = r"\b" + re.escape(term) + r"\b"
        sanitized = re.sub(pattern, replacement, sanitized, flags=re.IGNORECASE)
    return sanitized