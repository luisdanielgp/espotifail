"""
Django settings for espotifail project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modules.artists',
    'modules.albums',
    'modules.tracks',
    'modules.users',
    'rest_framework',
    'django_filters',
    'rest_framework_docs'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'espotifail.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'espotifail.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'espotifail',
        'USER': 'admin_espotifail',
        'PASSWORD': 'admin_espotifail',
        'HOST': 'localhost',
        'PORT': 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

COUNTRIES = (
    ("ALB", "Albania"),
    ("DZA", "Algeria"),
    ("ASM", "American Samoa"),
    ("AND", "Andorra"),
    ("AGO", "Angola"),
    ("AIA", "Anguilla"),
    ("ATA", "Antarctica"),
    ("ATG", "Antigua and Barbuda"),
    ("ARG", "Argentina"),
    ("ARM", "Armenia"),
    ("ABW", "Aruba"),
    ("AUS", "Australia"),
    ("AUT", "Austria"),
    ("AZE", "Azerbaijan"),
    ("BHS", "Bahamas"),
    ("BHR", "Bahrain"),
    ("BGD", "Bangladesh"),
    ("BRB", "Barbados"),
    ("BLR", "Belarus"),
    ("BEL", "Belgium"),
    ("BLZ", "Belize"),
    ("BEN", "Benin"),
    ("BMU", "Bermuda"),
    ("BTN", "Bhutan"),
    ("BOL", "Bolivia, Plurinational State of"),
    ("BES", "Bonaire, Sint Eustatius and Saba"),
    ("BIH", "Bosnia and Herzegovina"),
    ("BWA", "Botswana"),
    ("BVT", "Bouvet Island"),
    ("BRA", "Brazil"),
    ("IOT", "British Indian Ocean Territory"),
    ("BRN", "Brunei Darussalam"),
    ("BGR", "Bulgaria"),
    ("BFA", "Burkina Faso"),
    ("BDI", "Burundi"),
    ("KHM", "Cambodia"),
    ("CMR", "Cameroon"),
    ("CAN", "Canada"),
    ("CPV", "Cape Verde"),
    ("CYM", "Cayman Islands"),
    ("CAF", "Central African Republic"),
    ("TCD", "Chad"),
    ("CHL", "Chile"),
    ("CHN", "China"),
    ("CXR", "Christmas Island"),
    ("CCK", "Cocos (Keeling) Islands"),
    ("COL", "Colombia"),
    ("COM", "Comoros"),
    ("COG", "Congo"),
    ("COD", "Congo, the Democratic Republic of the"),
    ("COK", "Cook Islands"),
    ("CRI", "Costa Rica"),
    ("CIV", "Côte d'Ivoire"),
    ("HRV", "Croatia"),
    ("CUB", "Cuba"),
    ("CUW", "Curaçao"),
    ("CYP", "Cyprus"),
    ("CZE", "Czech Republic"),
    ("DNK", "Denmark"),
    ("DJI", "Djibouti"),
    ("DMA", "Dominica"),
    ("DOM", "Dominican Republic"),
    ("ECU", "Ecuador"),
    ("EGY", "Egypt"),
    ("SLV", "El Salvador"),
    ("GNQ", "Equatorial Guinea"),
    ("ERI", "Eritrea"),
    ("EST", "Estonia"),
    ("ETH", "Ethiopia"),
    ("FLK", "Falkland Islands (Malvinas)"),
    ("FRO", "Faroe Islands"),
    ("FJI", "Fiji"),
    ("FIN", "Finland"),
    ("FRA", "France"),
    ("GUF", "French Guiana"),
    ("PYF", "French Polynesia"),
    ("ATF", "French Southern Territories"),
    ("GAB", "Gabon"),
    ("GMB", "Gambia"),
    ("GEO", "Georgia"),
    ("DEU", "Germany"),
    ("GHA", "Ghana"),
    ("GIB", "Gibraltar"),
    ("GRC", "Greece"),
    ("GRL", "Greenland"),
    ("GRD", "Grenada"),
    ("GLP", "Guadeloupe"),
    ("GUM", "Guam"),
    ("GTM", "Guatemala"),
    ("GGY", "Guernsey"),
    ("GIN", "Guinea"),
    ("GNB", "Guinea-Bissau"),
    ("GUY", "Guyana"),
    ("HTI", "Haiti"),
    ("HMD", "Heard Island and McDonald Islands"),
    ("VAT", "Holy See (Vatican City State)"),
    ("HND", "Honduras"),
    ("HKG", "Hong Kong"),
    ("HUN", "Hungary"),
    ("ISL", "Iceland"),
    ("IND", "India"),
    ("IDN", "Indonesia"),
    ("IRN", "Iran, Islamic Republic of"),
    ("IRQ", "Iraq"),
    ("IRL", "Ireland"),
    ("IMN", "Isle of Man"),
    ("ISR", "Israel"),
    ("ITA", "Italy"),
    ("JAM", "Jamaica"),
    ("JPN", "Japan"),
    ("JEY", "Jersey"),
    ("JOR", "Jordan"),
    ("KAZ", "Kazakhstan"),
    ("KEN", "Kenya"),
    ("KIR", "Kiribati"),
    ("PRK", "Korea, Democratic People's Republic of"),
    ("KOR", "Korea, Republic of"),
    ("KWT", "Kuwait"),
    ("KGZ", "Kyrgyzstan"),
    ("LAO", "Lao People's Democratic Republic"),
    ("LVA", "Latvia"),
    ("LBN", "Lebanon"),
    ("LSO", "Lesotho"),
    ("LBR", "Liberia"),
    ("LBY", "Libya"),
    ("LIE", "Liechtenstein"),
    ("LTU", "Lithuania"),
    ("LUX", "Luxembourg"),
    ("MAC", "Macao"),
    ("MKD", "Macedonia, the former Yugoslav Republic of"),
    ("MDG", "Madagascar"),
    ("MWI", "Malawi"),
    ("MYS", "Malaysia"),
    ("MDV", "Maldives"),
    ("MLI", "Mali"),
    ("MLT", "Malta"),
    ("MHL", "Marshall Islands"),
    ("MTQ", "Martinique"),
    ("MRT", "Mauritania"),
    ("MUS", "Mauritius"),
    ("MYT", "Mayotte"),
    ("MEX", "Mexico"),
    ("FSM", "Micronesia, Federated States of"),
    ("MDA", "Moldova, Republic of"),
    ("MCO", "Monaco"),
    ("MNG", "Mongolia"),
    ("MNE", "Montenegro"),
    ("MSR", "Montserrat"),
    ("MAR", "Morocco"),
    ("MOZ", "Mozambique"),
    ("MMR", "Myanmar"),
    ("NAM", "Namibia"),
    ("NRU", "Nauru"),
    ("NPL", "Nepal"),
    ("NLD", "Netherlands"),
    ("NCL", "New Caledonia"),
    ("NZL", "New Zealand"),
    ("NIC", "Nicaragua"),
    ("NER", "Niger"),
    ("NGA", "Nigeria"),
    ("NIU", "Niue"),
    ("NFK", "Norfolk Island"),
    ("MNP", "Northern Mariana Islands"),
    ("NOR", "Norway"),
    ("OMN", "Oman"),
    ("PAK", "Pakistan"),
    ("PLW", "Palau"),
    ("PSE", "Palestinian Territory, Occupied"),
    ("PAN", "Panama"),
    ("PNG", "Papua New Guinea"),
    ("PRY", "Paraguay"),
    ("PER", "Peru"),
    ("PHL", "Philippines"),
    ("PCN", "Pitcairn"),
    ("POL", "Poland"),
    ("PRT", "Portugal"),
    ("PRI", "Puerto Rico"),
    ("QAT", "Qatar"),
    ("REU", "Réunion"),
    ("ROU", "Romania"),
    ("RUS", "Russian Federation"),
    ("RWA", "Rwanda"),
    ("BLM", "Saint Barthélemy"),
    ("SHN", "Saint Helena, Ascension and Tristan da Cunha"),
    ("KNA", "Saint Kitts and Nevis"),
    ("LCA", "Saint Lucia"),
    ("MAF", "Saint Martin (French part)"),
    ("SPM", "Saint Pierre and Miquelon"),
    ("VCT", "Saint Vincent and the Grenadines"),
    ("WSM", "Samoa"),
    ("SMR", "San Marino"),
    ("STP", "Sao Tome and Principe"),
    ("SAU", "Saudi Arabia"),
    ("SEN", "Senegal"),
    ("SRB", "Serbia"),
    ("SYC", "Seychelles"),
    ("SLE", "Sierra Leone"),
    ("SGP", "Singapore"),
    ("SXM", "Sint Maarten (Dutch part)"),
    ("SVK", "Slovakia"),
    ("SVN", "Slovenia"),
    ("SLB", "Solomon Islands"),
    ("SOM", "Somalia"),
    ("ZAF", "South Africa"),
    ("SGS", "South Georgia and the South Sandwich Islands"),
    ("SSD", "South Sudan"),
    ("ESP", "Spain"),
    ("LKA", "Sri Lanka"),
    ("SDN", "Sudan"),
    ("SUR", "Suriname"),
    ("SJM", "Svalbard and Jan Mayen"),
    ("SWZ", "Swaziland"),
    ("SWE", "Sweden"),
    ("CHE", "Switzerland"),
    ("SYR", "Syrian Arab Republic"),
    ("TWN", "Taiwan, Province of China"),
    ("TJK", "Tajikistan"),
    ("TZA", "Tanzania, United Republic of"),
    ("THA", "Thailand"),
    ("TLS", "Timor-Leste"),
    ("TGO", "Togo"),
    ("TKL", "Tokelau"),
    ("TON", "Tonga"),
    ("TTO", "Trinidad and Tobago"),
    ("TUN", "Tunisia"),
    ("TUR", "Turkey"),
    ("TKM", "Turkmenistan"),
    ("TCA", "Turks and Caicos Islands"),
    ("TUV", "Tuvalu"),
    ("UGA", "Uganda"),
    ("UKR", "Ukraine"),
    ("ARE", "United Arab Emirates"),
    ("GBR", "United Kingdom"),
    ("USA", "United States"),
    ("UMI", "United States Minor Outlying Islands"),
    ("URY", "Uruguay"),
    ("UZB", "Uzbekistan"),
    ("VUT", "Vanuatu"),
    ("VEN", "Venezuela, Bolivarian Republic of"),
    ("VNM", "Viet Nam"),
    ("VGB", "Virgin Islands, British"),
    ("VIR", "Virgin Islands, U.S."),
    ("WLF", "Wallis and Futuna"),
    ("ESH", "Western Sahara"),
    ("YEM", "Yemen"),
    ("ZMB", "Zambia"),
    ("ZWE", "Zimbabwe"))
