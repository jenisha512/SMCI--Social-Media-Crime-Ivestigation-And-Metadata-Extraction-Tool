def scan_text_for_crime(text_content):
    """Scans text for suspicious keywords."""
    
    # Expanded Keyword Database
    crime_dictionary = {
        "drugs": ["weed", "cocaine", "delivery", "stash", "grams", "pills", "dealer","lsd","heroine","meth","ecstasy","opium","fentanyl","marijuana","hashish","cannabis","amphetamine","mdma","psilocybin","ketamine","cannabis oil","synthetic cannabinoids"],
        "violence": ["kill", "shoot", "gun", "knife", "attack", "murder", "bomb","assault","homicide","domestic violence","child abuse","sexual assault","gang","terrorism","mass shooting","stabbing","robbery","carjacking","armed robbery","home invasion","kidnapping","hostage","manslaughter","assassination","extortion","threat","harassment","bullying","cyberbullying"],
        "fraud": ["bank", "password", "credit card", "transfer", "urgent", "account", "wire", "scam","phishing","identity theft","investment fraud","insurance fraud","tax fraud","healthcare fraud","charity fraud","pyramid scheme","ponzi scheme","advance fee fraud","credit card fraud","debit card fraud","check fraud","online fraud","mobile payment fraud","gift card fraud","loan fraud","mortgage fraud","securities fraud","corporate fraud","government fraud","welfare fraud","social security fraud","unemployment fraud","benefits fraud","tax evasion","money laundering"],
        "cyber": ["hack", "ddos", "malware", "botnet", "bitcoin", "phishing", "trojan", "ransomware", "exploit", "vulnerability", "zero-day", "backdoor", "keylogger", "spyware", "rootkit", "cryptojacking", "social engineering", "data breach", "cyber attack", "cybercrime", "cybersecurity", "cyber threat", "cyber espionage", "cyber warfare", "cyberbullying", "cyberstalking", "cyber harassment", "cyber extortion", "cyber fraud", "cyber identity theft", "cyber money laundering"],
        "human_trafficking": ["visa", "passport", "border", "smuggle", "transport", "recruit", "exploit", "trafficking", "sex trafficking", "labor trafficking", "child trafficking", "forced labor", "debt bondage", "domestic servitude", "organ trafficking", "trafficking in persons", "human smuggling", "human trafficking ring", "human trafficking network", "human trafficking victim", "human trafficking survivor", "human trafficking awareness", "human trafficking prevention", "human trafficking intervention", "human trafficking prosecution", "human trafficking legislation", "human trafficking policy", "human trafficking research", "human trafficking statistics", "human trafficking trends", "human trafficking hotspots", "human trafficking routes", "human trafficking methods", "human trafficking indicators", "human trafficking red flags", "human trafficking warning signs", "human trafficking resources", "human trafficking support", "human trafficking organizations", "human trafficking campaigns"],
    }
    
    detected_crimes = {}
    text_lower = text_content.lower()
    
    for category, keywords in crime_dictionary.items():
        found = [word for word in keywords if word in text_lower]
        if found:
            detected_crimes[category] = found
            
    return detected_crimes