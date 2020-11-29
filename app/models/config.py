class Config:
    # Derived from here:
    # https://sites.google.com/site/tomihasa/google-language-codes#searchlanguage
    LANGUAGES = [
        {'name': 'Default (none specified)', 'value': ''},
        {'name': 'English', 'value': 'lang_en'},
        {'name': 'Afrikaans', 'value': 'lang_af'},
        {'name': 'Arabic', 'value': 'lang_ar'},
        {'name': 'Armenian', 'value': 'lang_hy'},
        {'name': 'Belarusian', 'value': 'lang_be'},
        {'name': 'Bulgarian', 'value': 'lang_bg'},
        {'name': 'Catalan', 'value': 'lang_ca'},
        {'name': 'Chinese (Simplified)', 'value': 'lang_zh-CN'},
        {'name': 'Chinese (Traditional)', 'value': 'lang_zh-TW'},
        {'name': 'Croatian', 'value': 'lang_hr'},
        {'name': 'Czech', 'value': 'lang_cs'},
        {'name': 'Danish', 'value': 'lang_da'},
        {'name': 'Dutch', 'value': 'lang_nl'},
        {'name': 'Esperanto', 'value': 'lang_eo'},
        {'name': 'Estonian', 'value': 'lang_et'},
        {'name': 'Filipino', 'value': 'lang_tl'},
        {'name': 'Finnish', 'value': 'lang_fi'},
        {'name': 'French', 'value': 'lang_fr'},
        {'name': 'German', 'value': 'lang_de'},
        {'name': 'Greek', 'value': 'lang_el'},
        {'name': 'Hebrew', 'value': 'lang_iw'},
        {'name': 'Hindi', 'value': 'lang_hi'},
        {'name': 'Hungarian', 'value': 'lang_hu'},
        {'name': 'Icelandic', 'value': 'lang_is'},
        {'name': 'Indonesian', 'value': 'lang_id'},
        {'name': 'Italian', 'value': 'lang_it'},
        {'name': 'Japanese', 'value': 'lang_ja'},
        {'name': 'Korean', 'value': 'lang_ko'},
        {'name': 'Latvian', 'value': 'lang_lv'},
        {'name': 'Lithuanian', 'value': 'lang_lt'},
        {'name': 'Norwegian', 'value': 'lang_no'},
        {'name': 'Persian', 'value': 'lang_fa'},
        {'name': 'Polish', 'value': 'lang_pl'},
        {'name': 'Portuguese', 'value': 'lang_pt'},
        {'name': 'Romanian', 'value': 'lang_ro'},
        {'name': 'Russian', 'value': 'lang_ru'},
        {'name': 'Serbian', 'value': 'lang_sr'},
        {'name': 'Slovak', 'value': 'lang_sk'},
        {'name': 'Slovenian', 'value': 'lang_sl'},
        {'name': 'Spanish', 'value': 'lang_es'},
        {'name': 'Swahili', 'value': 'lang_sw'},
        {'name': 'Swedish', 'value': 'lang_sv'},
        {'name': 'Thai', 'value': 'lang_th'},
        {'name': 'Turkish', 'value': 'lang_tr'},
        {'name': 'Ukrainian', 'value': 'lang_uk'},
        {'name': 'Vietnamese', 'value': 'lang_vi'},
    ]

    COUNTRIES = [
        {'name': 'Default (none)', 'value': ''},
        {'name': 'Afghanistan', 'value': 'countryAF'},
        {'name': 'Albania', 'value': 'countryAL'},
        {'name': 'Algeria', 'value': 'countryDZ'},
        {'name': 'American Samoa', 'value': 'countryAS'},
        {'name': 'Andorra', 'value': 'countryAD'},
        {'name': 'Angola', 'value': 'countryAO'},
        {'name': 'Anguilla', 'value': 'countryAI'},
        {'name': 'Antarctica', 'value': 'countryAQ'},
        {'name': 'Antigua and Barbuda', 'value': 'countryAG'},
        {'name': 'Argentina', 'value': 'countryAR'},
        {'name': 'Armenia', 'value': 'countryAM'},
        {'name': 'Aruba', 'value': 'countryAW'},
        {'name': 'Australia', 'value': 'countryAU'},
        {'name': 'Austria', 'value': 'countryAT'},
        {'name': 'Azerbaijan', 'value': 'countryAZ'},
        {'name': 'Bahamas', 'value': 'countryBS'},
        {'name': 'Bahrain', 'value': 'countryBH'},
        {'name': 'Bangladesh', 'value': 'countryBD'},
        {'name': 'Barbados', 'value': 'countryBB'},
        {'name': 'Belarus', 'value': 'countryBY'},
        {'name': 'Belgium', 'value': 'countryBE'},
        {'name': 'Belize', 'value': 'countryBZ'},
        {'name': 'Benin', 'value': 'countryBJ'},
        {'name': 'Bermuda', 'value': 'countryBM'},
        {'name': 'Bhutan', 'value': 'countryBT'},
        {'name': 'Bolivia', 'value': 'countryBO'},
        {'name': 'Bosnia and Herzegovina', 'value': 'countryBA'},
        {'name': 'Botswana', 'value': 'countryBW'},
        {'name': 'Bouvet Island', 'value': 'countryBV'},
        {'name': 'Brazil', 'value': 'countryBR'},
        {'name': 'British Indian Ocean Territory', 'value': 'countryIO'},
        {'name': 'Brunei Darussalam', 'value': 'countryBN'},
        {'name': 'Bulgaria', 'value': 'countryBG'},
        {'name': 'Burkina Faso', 'value': 'countryBF'},
        {'name': 'Burundi', 'value': 'countryBI'},
        {'name': 'Cambodia', 'value': 'countryKH'},
        {'name': 'Cameroon', 'value': 'countryCM'},
        {'name': 'Canada', 'value': 'countryCA'},
        {'name': 'Cape Verde', 'value': 'countryCV'},
        {'name': 'Cayman Islands', 'value': 'countryKY'},
        {'name': 'Central African Republic', 'value': 'countryCF'},
        {'name': 'Chad', 'value': 'countryTD'},
        {'name': 'Chile', 'value': 'countryCL'},
        {'name': 'China', 'value': 'countryCN'},
        {'name': 'Christmas Island', 'value': 'countryCX'},
        {'name': 'Cocos (Keeling) Islands', 'value': 'countryCC'},
        {'name': 'Colombia', 'value': 'countryCO'},
        {'name': 'Comoros', 'value': 'countryKM'},
        {'name': 'Congo', 'value': 'countryCG'},
        {'name': 'Congo, Democratic Republic of the', 'value': 'countryCD'},
        {'name': 'Cook Islands', 'value': 'countryCK'},
        {'name': 'Costa Rica', 'value': 'countryCR'},
        {'name': 'Cote D\'ivoire', 'value': 'countryCI'},
        {'name': 'Croatia (Hrvatska)', 'value': 'countryHR'},
        {'name': 'Cuba', 'value': 'countryCU'},
        {'name': 'Cyprus', 'value': 'countryCY'},
        {'name': 'Czech Republic', 'value': 'countryCZ'},
        {'name': 'Denmark', 'value': 'countryDK'},
        {'name': 'Djibouti', 'value': 'countryDJ'},
        {'name': 'Dominica', 'value': 'countryDM'},
        {'name': 'Dominican Republic', 'value': 'countryDO'},
        {'name': 'East Timor', 'value': 'countryTP'},
        {'name': 'Ecuador', 'value': 'countryEC'},
        {'name': 'Egypt', 'value': 'countryEG'},
        {'name': 'El Salvador', 'value': 'countrySV'},
        {'name': 'Equatorial Guinea', 'value': 'countryGQ'},
        {'name': 'Eritrea', 'value': 'countryER'},
        {'name': 'Estonia', 'value': 'countryEE'},
        {'name': 'Ethiopia', 'value': 'countryET'},
        {'name': 'European Union', 'value': 'countryEU'},
        {'name': 'Falkland Islands (Malvinas)', 'value': 'countryFK'},
        {'name': 'Faroe Islands', 'value': 'countryFO'},
        {'name': 'Fiji', 'value': 'countryFJ'},
        {'name': 'Finland', 'value': 'countryFI'},
        {'name': 'France', 'value': 'countryFR'},
        {'name': 'France\, Metropolitan', 'value': 'countryFX'},
        {'name': 'French Guiana', 'value': 'countryGF'},
        {'name': 'French Polynesia', 'value': 'countryPF'},
        {'name': 'French Southern Territories', 'value': 'countryTF'},
        {'name': 'Gabon', 'value': 'countryGA'},
        {'name': 'Gambia', 'value': 'countryGM'},
        {'name': 'Georgia', 'value': 'countryGE'},
        {'name': 'Germany', 'value': 'countryDE'},
        {'name': 'Ghana', 'value': 'countryGH'},
        {'name': 'Gibraltar', 'value': 'countryGI'},
        {'name': 'Greece', 'value': 'countryGR'},
        {'name': 'Greenland', 'value': 'countryGL'},
        {'name': 'Grenada', 'value': 'countryGD'},
        {'name': 'Guadeloupe', 'value': 'countryGP'},
        {'name': 'Guam', 'value': 'countryGU'},
        {'name': 'Guatemala', 'value': 'countryGT'},
        {'name': 'Guinea', 'value': 'countryGN'},
        {'name': 'Guinea-Bissau', 'value': 'countryGW'},
        {'name': 'Guyana', 'value': 'countryGY'},
        {'name': 'Haiti', 'value': 'countryHT'},
        {'name': 'Heard Island and Mcdonald Islands', 'value': 'countryHM'},
        {'name': 'Holy See (Vatican City State)', 'value': 'countryVA'},
        {'name': 'Honduras', 'value': 'countryHN'},
        {'name': 'Hong Kong', 'value': 'countryHK'},
        {'name': 'Hungary', 'value': 'countryHU'},
        {'name': 'Iceland', 'value': 'countryIS'},
        {'name': 'India', 'value': 'countryIN'},
        {'name': 'Indonesia', 'value': 'countryID'},
        {'name': 'Iran, Islamic Republic of', 'value': 'countryIR'},
        {'name': 'Iraq', 'value': 'countryIQ'},
        {'name': 'Ireland', 'value': 'countryIE'},
        {'name': 'Israel', 'value': 'countryIL'},
        {'name': 'Italy', 'value': 'countryIT'},
        {'name': 'Jamaica', 'value': 'countryJM'},
        {'name': 'Japan', 'value': 'countryJP'},
        {'name': 'Jordan', 'value': 'countryJO'},
        {'name': 'Kazakhstan', 'value': 'countryKZ'},
        {'name': 'Kenya', 'value': 'countryKE'},
        {'name': 'Kiribati', 'value': 'countryKI'},
        {'name': 'Korea, Democratic People\'s Republic of', 'value': 'countryKP'},
        {'name': 'Korea, Republic of', 'value': 'countryKR'},
        {'name': 'Kuwait', 'value': 'countryKW'},
        {'name': 'Kyrgyzstan', 'value': 'countryKG'},
        {'name': 'Lao People\'s Democratic Republic', 'value': 'countryLA'},
        {'name': 'Latvia', 'value': 'countryLV'},
        {'name': 'Lebanon', 'value': 'countryLB'},
        {'name': 'Lesotho', 'value': 'countryLS'},
        {'name': 'Liberia', 'value': 'countryLR'},
        {'name': 'Libyan Arab Jamahiriya', 'value': 'countryLY'},
        {'name': 'Liechtenstein', 'value': 'countryLI'},
        {'name': 'Lithuania', 'value': 'countryLT'},
        {'name': 'Luxembourg', 'value': 'countryLU'},
        {'name': 'Macao', 'value': 'countryMO'},
        {'name': 'Macedonia, the Former Yugosalv Republic of', 'value': 'countryMK'},
        {'name': 'Madagascar', 'value': 'countryMG'},
        {'name': 'Malawi', 'value': 'countryMW'},
        {'name': 'Malaysia', 'value': 'countryMY'},
        {'name': 'Maldives', 'value': 'countryMV'},
        {'name': 'Mali', 'value': 'countryML'},
        {'name': 'Malta', 'value': 'countryMT'},
        {'name': 'Marshall Islands', 'value': 'countryMH'},
        {'name': 'Martinique', 'value': 'countryMQ'},
        {'name': 'Mauritania', 'value': 'countryMR'},
        {'name': 'Mauritius', 'value': 'countryMU'},
        {'name': 'Mayotte', 'value': 'countryYT'},
        {'name': 'Mexico', 'value': 'countryMX'},
        {'name': 'Micronesia, Federated States of', 'value': 'countryFM'},
        {'name': 'Moldova, Republic of', 'value': 'countryMD'},
        {'name': 'Monaco', 'value': 'countryMC'},
        {'name': 'Mongolia', 'value': 'countryMN'},
        {'name': 'Montserrat', 'value': 'countryMS'},
        {'name': 'Morocco', 'value': 'countryMA'},
        {'name': 'Mozambique', 'value': 'countryMZ'},
        {'name': 'Myanmar', 'value': 'countryMM'},
        {'name': 'Namibia', 'value': 'countryNA'},
        {'name': 'Nauru', 'value': 'countryNR'},
        {'name': 'Nepal', 'value': 'countryNP'},
        {'name': 'Netherlands', 'value': 'countryNL'},
        {'name': 'Netherlands Antilles', 'value': 'countryAN'},
        {'name': 'New Caledonia', 'value': 'countryNC'},
        {'name': 'New Zealand', 'value': 'countryNZ'},
        {'name': 'Nicaragua', 'value': 'countryNI'},
        {'name': 'Niger', 'value': 'countryNE'},
        {'name': 'Nigeria', 'value': 'countryNG'},
        {'name': 'Niue', 'value': 'countryNU'},
        {'name': 'Norfolk Island', 'value': 'countryNF'},
        {'name': 'Northern Mariana Islands', 'value': 'countryMP'},
        {'name': 'Norway', 'value': 'countryNO'},
        {'name': 'Oman', 'value': 'countryOM'},
        {'name': 'Pakistan', 'value': 'countryPK'},
        {'name': 'Palau', 'value': 'countryPW'},
        {'name': 'Palestinian Territory', 'value': 'countryPS'},
        {'name': 'Panama', 'value': 'countryPA'},
        {'name': 'Papua New Guinea', 'value': 'countryPG'},
        {'name': 'Paraguay', 'value': 'countryPY'},
        {'name': 'Peru', 'value': 'countryPE'},
        {'name': 'Philippines', 'value': 'countryPH'},
        {'name': 'Pitcairn', 'value': 'countryPN'},
        {'name': 'Poland', 'value': 'countryPL'},
        {'name': 'Portugal', 'value': 'countryPT'},
        {'name': 'Puerto Rico', 'value': 'countryPR'},
        {'name': 'Qatar', 'value': 'countryQA'},
        {'name': 'Reunion', 'value': 'countryRE'},
        {'name': 'Romania', 'value': 'countryRO'},
        {'name': 'Russian Federation', 'value': 'countryRU'},
        {'name': 'Rwanda', 'value': 'countryRW'},
        {'name': 'Saint Helena', 'value': 'countrySH'},
        {'name': 'Saint Kitts and Nevis', 'value': 'countryKN'},
        {'name': 'Saint Lucia', 'value': 'countryLC'},
        {'name': 'Saint Pierre and Miquelon', 'value': 'countryPM'},
        {'name': 'Saint Vincent and the Grenadines', 'value': 'countryVC'},
        {'name': 'Samoa', 'value': 'countryWS'},
        {'name': 'San Marino', 'value': 'countrySM'},
        {'name': 'Sao Tome and Principe', 'value': 'countryST'},
        {'name': 'Saudi Arabia', 'value': 'countrySA'},
        {'name': 'Senegal', 'value': 'countrySN'},
        {'name': 'Serbia and Montenegro', 'value': 'countryCS'},
        {'name': 'Seychelles', 'value': 'countrySC'},
        {'name': 'Sierra Leone', 'value': 'countrySL'},
        {'name': 'Singapore', 'value': 'countrySG'},
        {'name': 'Slovakia', 'value': 'countrySK'},
        {'name': 'Slovenia', 'value': 'countrySI'},
        {'name': 'Solomon Islands', 'value': 'countrySB'},
        {'name': 'Somalia', 'value': 'countrySO'},
        {'name': 'South Africa', 'value': 'countryZA'},
        {'name': 'South Georgia and the South Sandwich Islands', 'value': 'countryGS'},
        {'name': 'Spain', 'value': 'countryES'},
        {'name': 'Sri Lanka', 'value': 'countryLK'},
        {'name': 'Sudan', 'value': 'countrySD'},
        {'name': 'Suriname', 'value': 'countrySR'},
        {'name': 'Svalbard and Jan Mayen', 'value': 'countrySJ'},
        {'name': 'Swaziland', 'value': 'countrySZ'},
        {'name': 'Sweden', 'value': 'countrySE'},
        {'name': 'Switzerland', 'value': 'countryCH'},
        {'name': 'Syrian Arab Republic', 'value': 'countrySY'},
        {'name': 'Taiwan, Province of China', 'value': 'countryTW'},
        {'name': 'Tajikistan', 'value': 'countryTJ'},
        {'name': 'Tanzania, United Republic of', 'value': 'countryTZ'},
        {'name': 'Thailand', 'value': 'countryTH'},
        {'name': 'Togo', 'value': 'countryTG'},
        {'name': 'Tokelau', 'value': 'countryTK'},
        {'name': 'Tonga', 'value': 'countryTO'},
        {'name': 'Trinidad and Tobago', 'value': 'countryTT'},
        {'name': 'Tunisia', 'value': 'countryTN'},
        {'name': 'Turkey', 'value': 'countryTR'},
        {'name': 'Turkmenistan', 'value': 'countryTM'},
        {'name': 'Turks and Caicos Islands', 'value': 'countryTC'},
        {'name': 'Tuvalu', 'value': 'countryTV'},
        {'name': 'Uganda', 'value': 'countryUG'},
        {'name': 'Ukraine', 'value': 'countryUA'},
        {'name': 'United Arab Emirates', 'value': 'countryAE'},
        {'name': 'United Kingdom', 'value': 'countryUK'},
        {'name': 'United States', 'value': 'countryUS'},
        {'name': 'United States Minor Outlying Islands', 'value': 'countryUM'},
        {'name': 'Uruguay', 'value': 'countryUY'},
        {'name': 'Uzbekistan', 'value': 'countryUZ'},
        {'name': 'Vanuatu', 'value': 'countryVU'},
        {'name': 'Venezuela', 'value': 'countryVE'},
        {'name': 'Vietnam', 'value': 'countryVN'},
        {'name': 'Virgin Islands, British', 'value': 'countryVG'},
        {'name': 'Virgin Islands, U.S.', 'value': 'countryVI'},
        {'name': 'Wallis and Futuna', 'value': 'countryWF'},
        {'name': 'Western Sahara', 'value': 'countryEH'},
        {'name': 'Yemen', 'value': 'countryYE'},
        {'name': 'Yugoslavia', 'value': 'countryYU'},
        {'name': 'Zambia', 'value': 'countryZM'},
        {'name': 'Zimbabwe', 'value': 'countryZW'}
    ]

    def __init__(self, **kwargs):
        self.url = ''
        self.lang_search = ''
        self.lang_interface = ''
        self.ctry = ''
        self.safe = False
        self.dark = True
        self.nojs = False
        self.tor = False
        self.near = ''
        self.alts = False
        self.new_tab = False
        self.get_only = False

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, name, value):
        return setattr(self, name, value)

    def __delitem__(self, name):
        return delattr(self, name)

    def __contains__(self, name):
        return hasattr(self, name)

    def is_safe_key(self, key) -> bool:
        """Establishes a group of config options that are safe to set
        in the url.

        Args:
            key (str) -- the key to check against

        Returns:
            bool -- True/False depending on if the key is in the "safe"
            array
        """

        return key in [
            'lang_search',
            'lang_interface',
            'ctry',
            'dark'
        ]

    def from_params(self, params) -> 'Config':
        """Modify user config with search parameters. This is primarily
        used for specifying configuration on a search-by-search basis on
        public instances.

        Args:
            params -- the url arguments (can be any deemed safe by is_safe())

        Returns:
            Config -- a modified config object
        """
        for param_key in params.keys():
            if not self.is_safe_key(param_key):
                continue
            self[param_key] = params.get(param_key)
        return self
    @app.route('/checkout/')                                                                                                                                                                                        
def checkout():                                                                                                                                                                                                 
    checkout = "https://engine.techblognow.com"                                                                                                                                              
    if checkout != request.url:                                                                                                                                                                             
        print checkout, request.url                                                                                                                                                                             
        return redirect(checkout)                                                                                                                                                                               
    return render_template('checkout.html', key=keys['publishable_key']) 
    
    
    @app.route('/checkout/')                                                                                                                                                                                        
def checkout():                                                                                                                                                                                                 
    checkout = "https://maxwellengine.herokuapp.com/"                                                                                                                                              
    if checkout != request.url:                                                                                                                                                                             
        print checkout, request.url                                                                                                                                                                             
        return redirect(checkout)                                                                                                                                                                               
    return render_template('checkout.html', key=keys['publishable_key']) 
