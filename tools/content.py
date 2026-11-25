"""Editable copy for the generated pages: FAQs, ShiftFlow industry pages and Insights articles.

Loaded by build_site.py. Plain data only, so it is safe to edit the wording here and rebuild with
    python -I tools/build_site.py .
Answers may contain simple HTML (links, <b>); the FAQ structured data uses the plain text.
"""

# ---------- FAQs ----------
HOME_FAQ = [
    ("Where is BTree based?",
     "We are based in Bradford, in the United Kingdom, and work with businesses across the UK."),
    ("What size of business do you work with?",
     "Businesses of every size, from a single shop or office to multi-site organisations. Most of our clients do not "
     "have a large IT team of their own, so we act as an extension of theirs."),
    ("Can you look after everything, or just a single project?",
     "Either. Some clients bring us in for one project, such as a Microsoft 365 migration or a new application. Others "
     "ask us to look after their network, security and cloud services on an ongoing basis."),
    ("What is ShiftFlow?",
     'ShiftFlow is our own workforce platform for shift-based businesses: rotas, clock-ins, timesheets and HR in one '
     'place, with UK working time rules checked automatically. <a href="shiftflow/">See ShiftFlow</a>.'),
    ("How do we get started?",
     'Tell us what you need using the <a href="#contact">contact form</a> or email '
     '<a href="mailto:info@btree.uk">info@btree.uk</a>. We will arrange a short conversation to understand where you '
     'are today, then suggest a practical next step, with no obligation.'),
]

SERVICE_FAQ = {
    "software-development": [
        ("How much does custom software cost?",
         "It depends on what the software needs to do. After a short discovery conversation we send a written proposal "
         "with options, costs and timings, so you know exactly what you are getting before any work starts."),
        ("How long does it take to build a business application?",
         "A focused integration or internal tool can take a few weeks. Larger products are delivered in stages over a "
         "few months, with something usable early so your team can try it and give feedback."),
        ("Can you connect the systems we already use?",
         "Yes. Integrations are a big part of what we do, for example linking accounting, HR, point of sale and CRM "
         "systems through their APIs, so data moves between them without anyone re-typing it."),
        ("Do you support the software after it goes live?",
         "Yes. We look after what we build, with maintenance, security updates, monitoring and improvements as your "
         "business changes."),
    ],
    "ai-adoption": [
        ("Is it safe to use AI tools with our business data?",
         "It can be, if you choose the right tools and set them up properly. Business versions of AI tools, such as "
         "Microsoft 365 Copilot, work inside your own Microsoft 365 environment and only show people content they "
         "already have permission to see. Free consumer tools may handle your data differently. We help you choose "
         "tools, check permissions and write a clear policy on what staff can share."),
        ("Do we need Microsoft 365 Copilot?",
         "Not necessarily. Copilot works best when your files and permissions in Microsoft 365 are well organised. "
         "An AI readiness assessment shows whether Copilot, another tool or a simple automation will give you the best "
         "return."),
        ("Where should a small business start with AI?",
         "Pick one or two repetitive, time-consuming tasks, such as drafting replies, summarising documents or "
         "re-typing data, try an AI tool on them with a small group, and measure the time saved. Put a short AI use "
         "policy in place at the same time."),
        ("Does UK GDPR apply when we use AI?",
         "Yes. If an AI tool processes personal information, the usual data protection rules still apply, so you need "
         "to know what data goes where, have a lawful basis and keep it secure. For higher-risk uses, a data protection "
         "impact assessment is a good idea. We build this into every AI roll-out."),
    ],
    "networks": [
        ("What is the difference between business broadband and a leased line?",
         "Business broadband shares capacity with other users and is usually faster to download than to upload. A "
         "leased line is a dedicated connection with the same speed in both directions, guaranteed performance and a "
         "faster repair commitment. It costs more, so we help you decide which each site really needs."),
        ("Do we need a backup internet connection?",
         "If your tills, phones or cloud systems stop when the internet goes down, yes. A 4G or 5G backup that takes "
         "over automatically is usually inexpensive and keeps you trading while the main line is fixed."),
        ("Should our guest Wi-Fi be separate from our business network?",
         "Yes. Guests should never be on the same network as your tills, servers or staff devices. We set up separate "
         "staff and guest networks so one cannot reach the other."),
        ("Can you manage networks across several sites?",
         "Yes. We connect and manage multi-site networks centrally, with consistent firewall and Wi-Fi settings at "
         "every location and secure links between sites, remote workers and the cloud."),
    ],
    "cyber-security": [
        ("What is Cyber Essentials?",
         'Cyber Essentials is a UK government-backed certification that shows you have five basic security controls in '
         'place. Cyber Essentials Plus adds an independent technical check. Read our '
         '<a href="../../insights/cyber-essentials-explained/">plain-English guide to Cyber Essentials</a>.'),
        ("Is multi-factor authentication really necessary?",
         "Yes. Stolen or guessed passwords are one of the most common ways attackers get in, and multi-factor "
         "authentication stops most of those attacks. It is also required for cloud services under Cyber Essentials."),
        ("What should a small business fix first?",
         "Usually: turn on multi-factor authentication everywhere, keep devices and software updated, make sure backups "
         "work and are kept separate, stop using admin accounts for everyday work, and help staff spot phishing emails."),
        ("How often should we review our security?",
         "At least once a year, and whenever something significant changes, such as a new system, a new site or a move "
         "to the cloud. Cyber Essentials certification is also renewed every year."),
    ],
    "microsoft-365-azure": [
        ("Can you move us from Google Workspace to Microsoft 365?",
         "Yes. We migrate email, calendars, contacts and files from Google Workspace, other email providers and "
         'on-premises Exchange. See our <a href="../../insights/microsoft-365-migration-checklist/">Microsoft 365 '
         'migration checklist</a>.'),
        ("Will we lose email during the migration?",
         "No. We copy your existing email first, then switch incoming mail over at a planned time, usually outside "
         "working hours, and copy anything that arrived in between. Staff carry on working throughout."),
        ("Which Microsoft 365 plan do we need?",
         "For most businesses with up to 300 users it is one of the Business plans. Business Premium includes device "
         "management with Intune and stronger identity and security controls, which we recommend for most clients. We "
         "check what you actually need so you do not pay for unused licences."),
        ("Do you support on-premises Exchange and Active Directory?",
         "Yes, including hybrid set-ups that combine on-premises and cloud, clean-ups, and migrations to Microsoft 365 "
         "and Entra ID."),
    ],
    "aws": [
        ("How can we reduce our AWS bill?",
         "The biggest savings usually come from right-sizing servers, switching off resources nobody uses, moving "
         "steady workloads to savings plans and storing data in the right storage class. We review your account and "
         "give you a prioritised list."),
        ("Is AWS or Azure better for our business?",
         "Both are excellent. If you rely heavily on Microsoft 365 and Windows, Azure often fits more naturally; AWS "
         "has a very broad range of services and is a common choice for software products. We work with both and will "
         "recommend what suits you."),
        ("Can you take over an AWS account that someone else set up?",
         "Yes. We start with an architecture review covering security, reliability and cost, fix anything urgent, then "
         "document the environment so it is no longer dependent on one person."),
        ("What is infrastructure as code?",
         "It means your servers, networks and settings are defined in files, using tools such as Terraform or "
         "CloudFormation, instead of being clicked together by hand. Environments become repeatable, reviewable and "
         "easy to rebuild."),
    ],
}

SHIFTFLOW_FAQ = [
    ("What is ShiftFlow?",
     "ShiftFlow is a workforce platform for UK businesses that run on shifts. It brings rotas, clock-ins, timesheets, "
     "holiday, documents and HR records together in one place, so the hours on the rota, the punches at the door and "
     "the figures sent to payroll always agree."),
    ("Does ShiftFlow check UK working time rules?",
     "Yes. Every rota is checked before it is published, including 11 hours rest between shifts, the 48-hour average "
     "week, minimum breaks, limits for under-18s and visa weekly hour caps. Errors block publishing and warnings are "
     "shown, and each rule can be tuned for each site."),
    ("What devices does ShiftFlow work on?",
     "Managers use ShiftFlow in a web browser. Staff clock in on an iPad or Android tablet running the kiosk app, and "
     "use the employee app on iOS or Android to see shifts, book holiday and swap shifts."),
    ("What happens if the internet goes down?",
     "The kiosk keeps working. Clock-ins are stored on the tablet and sent as soon as the connection returns."),
    ("Can ShiftFlow handle several sites?",
     "Yes. Staff can have a home site and other sites they work at, double bookings across sites are blocked, open "
     "shifts can be offered across sites, and settings can be set once for the business and changed for each site."),
    ("Does ShiftFlow work with our payroll?",
     "Approved hours go into a pay run export that you can give to your payroll provider or import into your payroll "
     "software."),
    ("Can staff sign in with their Microsoft account?",
     "Yes. ShiftFlow supports single sign-on with Microsoft Entra ID or any OIDC provider, as well as authenticator "
     "app multi-factor authentication."),
    ("How much does ShiftFlow cost?",
     'Pricing depends on the size of your team and the parts you use. <a href="#contact">Book a demo</a> and we will '
     'show you ShiftFlow and give you a quote.'),
]

# ---------- ShiftFlow industry pages (/shiftflow/<slug>/) ----------
# "match" is the industry name in SF_INDUSTRIES (build_site.py), used for the shift map card.
SF_PAGES = [
    {
        "slug": "hospitality", "match": "Hospitality", "short": "Hospitality",
        "title": "Rota and HR software for restaurants, bars and hotels | ShiftFlow",
        "desc": "ShiftFlow rotas, clock-ins and HR for UK restaurants, bars, cafes and hotels: shifts past midnight, live "
                "labour cost against sales, food hygiene certificates and open shifts across venues.",
        "h1": 'Rotas for restaurants, bars and hotels <span class="grad">that work past midnight.</span>',
        "sub": "Late finishes, split rotas, busy weekends and staff who work across venues. ShiftFlow was built in "
               "hospitality, where shifts are at their most complicated.",
        "points": [
            ("Trading days past midnight", "A 17:00 to 02:00 shift stays on the night it started, in the right week "
             "and the right pay period."),
            ("Labour cost against sales", "Hours, cost, wage percentage and sales per labour hour update live as you "
             "build the rota."),
            ("Certificates by position", "Food hygiene and management certificates are checked for the roles that "
             "need them before the rota goes out."),
            ("Last-minute cover", "Broadcast open shifts across your venues. Staff claim them and you confirm, and "
             "swaps go to a manager to approve."),
            ("One person, several roles", "A server who also works the bar can hold both positions, each with its own "
             "pay rate."),
            ("Weather on the rota", "The forecast sits on every day, so you can staff up for a sunny Saturday."),
        ],
        "faq": [
            ("Does ShiftFlow work for venues that close after midnight?",
             "Yes. Your trading day ends when your last shift does, not at midnight, so late shifts stay on the right "
             "day for rotas, timesheets and reports."),
            ("Can I see labour cost as a percentage of sales?",
             "Yes. The rota shows hours, cost, wage percentage and sales per labour hour as you plan, and the reports "
             "compare sales against labour."),
            ("Can staff work at more than one of our venues?",
             "Yes. Staff have a home site and other sites they can work at, and ShiftFlow blocks anyone being booked at "
             "two venues at the same time."),
        ],
    },
    {
        "slug": "retail", "match": "Retail", "short": "Retail",
        "title": "Rota and HR software for shops and retail chains | ShiftFlow",
        "desc": "ShiftFlow rotas, clock-ins and HR for UK retailers: cover for opening hours, seasonal peaks, under-18 "
                "Saturday staff and teams that work across branches.",
        "h1": 'Rotas for shops that <span class="grad">cover every opening hour.</span>',
        "sub": "From a single shop to a chain of branches, plan cover for opening hours and seasonal peaks, and let "
               "staff manage their own availability, swaps and holiday from their phone.",
        "points": [
            ("See the gaps", "The coverage heatmap shows how many people are on the shop floor hour by hour, so gaps "
             "and overstaffing stand out."),
            ("Peaks without the panic", "Start from shift templates or copy last week, then broadcast extra shifts for "
             "busy periods for staff to claim."),
            ("Branches working together", "Staff can work at several branches, with transfers recorded and double "
             "bookings blocked."),
            ("Young workers", "Daily hours and night work limits for under-18s are checked before the rota is "
             "published."),
            ("Availability up front", "Staff set their availability in the app, and it shows on the rota while you "
             "plan."),
            ("Settings that inherit", "Set the rules once for the business and adjust them for each branch."),
        ],
        "faq": [
            ("Can staff work across several of our shops?",
             "Yes. Each person has a home shop and can be added to others. Transfers between shops keep an audit trail."),
            ("Does ShiftFlow handle Saturday staff who are under 18?",
             "Yes. ShiftFlow checks daily hours and night work limits for young workers before a rota is published."),
            ("Can staff tell us when they are available?",
             "Yes. Staff set their availability in the employee app, and managers see it on the rota while planning."),
        ],
    },
    {
        "slug": "care", "match": "Health and social care", "short": "Care",
        "title": "Rota and HR software for care homes and home care | ShiftFlow",
        "desc": "ShiftFlow rotas, clock-ins and HR for UK care providers: round-the-clock rotas, night shifts, Right to "
                "Work and visa hour checks, document expiry warnings and secure staff records.",
        "h1": 'Round-the-clock rotas <span class="grad">for care teams.</span>',
        "sub": "Early, late and night shifts, training that must stay in date and staff records that must stay "
               "secure. ShiftFlow keeps your rota covered and your paperwork in order.",
        "points": [
            ("Nights done properly", "Night shifts that cross midnight are handled correctly, with 11 hours rest "
             "between shifts checked automatically."),
            ("Right to Work, tracked", "Right to Work checks with reminders 30, 14 and 7 days before permission "
             "expires."),
            ("Visa hour caps", "Weekly hour limits from Right to Work are checked across every site before the rota is "
             "published."),
            ("Documents in date", "An encrypted document library with expiry warnings, so certificates and other "
             "documents do not quietly lapse."),
            ("Cover when someone calls in sick", "Broadcast open shifts across your services and let staff claim them."),
            ("Sensitive data protected", "Encryption, single sign-on, multi-factor authentication, roles scoped to "
             "sites and a full audit log."),
        ],
        "faq": [
            ("Does ShiftFlow remind us when a member of staff's Right to Work is due to expire?",
             "Yes. ShiftFlow sends reminders 30, 14 and 7 days before the expiry date recorded on the Right to Work "
             "check."),
            ("Can ShiftFlow stop staff working more hours than their visa allows?",
             "ShiftFlow checks weekly hour caps from Right to Work records across all sites, and flags or blocks a rota "
             "that would break them, depending on how you set the rule."),
            ("How is staff information kept secure?",
             "Sensitive data and documents are encrypted, access is controlled by roles scoped to sites, sign-in can "
             "use single sign-on and multi-factor authentication, and every change is recorded in an audit log."),
        ],
    },
    {
        "slug": "warehousing-logistics", "match": "Warehousing and logistics", "short": "Warehousing",
        "title": "Shift planning and time clock software for warehouses | ShiftFlow",
        "desc": "ShiftFlow shift planning, clock-ins and timesheets for UK warehouses, distribution centres and "
                "logistics teams: rotating shifts, accurate clock-ins, offline kiosks and payroll-ready hours.",
        "h1": 'Shift planning and clock-ins <span class="grad">for busy warehouses.</span>',
        "sub": "Days, backs and nights, rotating patterns and big sites where the Wi-Fi does not always reach. "
               "ShiftFlow gets everyone clocked in accurately and the hours to payroll correctly.",
        "points": [
            ("Rotating patterns", "Build days, backs and nights from shift templates, or copy last week and adjust."),
            ("Accurate clock-ins", "PIN clock-in on a tablet at the door, with an optional photo and geofencing for "
             "extra confidence."),
            ("Works offline", "The kiosk keeps recording clock-ins when the connection drops and syncs when it "
             "returns."),
            ("Late and no-show rules", "Late arrivals, early leavers and no-shows are flagged using rules you set."),
            ("Rest and hours checked", "11 hours rest and the 48-hour average week are checked before the rota is "
             "published."),
            ("Payroll-ready hours", "Planned and actual hours side by side, approved in bulk and exported for "
             "payroll."),
        ],
        "faq": [
            ("Does the clock-in work where the Wi-Fi is patchy?",
             "Yes. The kiosk stores clock-ins on the tablet and sends them as soon as the connection returns."),
            ("Can we be confident the right person is clocking in?",
             "Each person clocks in with their own PIN, and you can switch on a photo at clock-in and geofencing."),
            ("Can we send approved hours to payroll?",
             "Yes. Once timesheets are approved, the hours go into a pay run export for your payroll."),
        ],
    },
    {
        "slug": "manufacturing", "match": "Manufacturing", "short": "Manufacturing",
        "title": "Shift rota and time and attendance software for manufacturing | ShiftFlow",
        "desc": "ShiftFlow shift rotas, time and attendance and HR for UK manufacturers: day and night shift patterns, "
                "overtime visibility, Working Time checks and planned against actual hours.",
        "h1": 'Shift patterns and overtime, <span class="grad">under control.</span>',
        "sub": "Day and night patterns, overtime that creeps up and Working Time limits to respect. ShiftFlow shows "
               "you the hours before they become a problem.",
        "points": [
            ("Patterns your way", "Twelve-hour days and nights, three-shift rotations or something of your own, built "
             "from templates."),
            ("Overtime in view", "Attendance and overtime reports, and planned against actual hours for every shift."),
            ("Working Time checks", "Rest between shifts, the 48-hour average week and limits for young workers, "
             "checked before you publish."),
            ("Clock-in at the gate", "A tablet kiosk with PIN clock-in, breaks and clock-out, even offline."),
            ("Bulk approval", "Clear the exceptions, then approve a whole week of timesheets in one click."),
            ("Reports you can share", "Every report prints and exports to CSV."),
        ],
        "faq": [
            ("Can ShiftFlow handle 12-hour shift patterns?",
             "Yes. Shift lengths and patterns are up to you, and rest between shifts is still checked."),
            ("Can we see overtime before it happens?",
             "Yes. Hours and cost update as you build the rota, and reports show attendance and overtime against what "
             "was planned."),
            ("Does it handle night shifts?",
             "Yes. Shifts can run past midnight and stay on the day they started, and night work limits for under-18s "
             "are checked."),
        ],
    },
    {
        "slug": "facilities-cleaning-security", "match": "Facilities, cleaning and security", "short": "Facilities",
        "title": "Rota and time tracking software for cleaning and security teams | ShiftFlow",
        "desc": "ShiftFlow rotas, clock-ins and HR for UK facilities, cleaning and security companies: staff across "
                "client sites, hours actually worked, licence and document expiry warnings.",
        "h1": 'Know who is on site, <span class="grad">at every client.</span>',
        "sub": "Early cleans, evening cleans and night security across many client sites. ShiftFlow shows who is where "
               "and pays only for the hours actually worked.",
        "points": [
            ("Many sites, one view", "Staff have a home site and extra sites, with every site and its team on a map."),
            ("Hours actually worked", "Planned against actual hours, with geofencing and an optional photo at "
             "clock-in."),
            ("Short and split shifts", "Early and evening cleans on the same day are easy to plan and easy to pay."),
            ("Licences in date", "Keep licences and certificates as documents with expiry dates and get warnings "
             "before they lapse."),
            ("Who is on now", "The dashboard shows who is on shift right now, across every site."),
            ("Announcements", "Post updates to a site or a position and see exactly who has read them."),
        ],
        "faq": [
            ("Can we see who is on site right now?",
             "Yes. The dashboard shows who is on shift now, and clock-ins appear as they happen."),
            ("Can we track licence expiry dates, such as SIA licences?",
             "Yes. Store licences and certificates as documents with an expiry date, and ShiftFlow warns you before "
             "they expire."),
            ("Can one person work at several client sites?",
             "Yes. Staff can be added to any number of sites, and ShiftFlow blocks double bookings across them."),
        ],
    },
]

# ---------- Insights articles (/insights/<slug>/) ----------
# body: HTML for the article. Keep facts checkable and link to the official source.
ARTICLES = [
    {
        "slug": "uk-working-time-rules-shift-workers",
        "title": "UK working time rules for shift workers: a guide for managers",
        "desc": "A plain-English guide to the Working Time Regulations for UK shift-based businesses: the 48-hour week, "
                "rest between shifts, breaks, night work, young workers and holiday.",
        "date": "2026-11-24", "minutes": 7, "topic": "Workforce", "related": ("ShiftFlow", "shiftflow/"),
        "body": """
<p>If you run a restaurant, shop, care home or warehouse, your rota has to respect the Working Time Regulations 1998. This guide sets out the main rules for workers in Great Britain in plain English. Northern Ireland has its own, very similar rules.</p>
<p class="note">This is general information, not legal advice. Rules change, so check <a href="https://www.gov.uk/maximum-weekly-working-hours" rel="noopener">GOV.UK</a> or <a href="https://www.acas.org.uk/working-hours" rel="noopener">Acas</a> for your situation.</p>

<h2>The 48-hour week</h2>
<p>Workers aged 18 and over cannot be made to work more than 48 hours a week on average. The average is normally worked out over 17 weeks, so a busy week can be balanced by quieter ones.</p>
<ul>
  <li>A worker can choose to <b>opt out</b> of the 48-hour limit. The opt-out must be voluntary and in writing, and they can cancel it by giving notice.</li>
  <li>You cannot dismiss or treat someone unfairly for refusing to opt out.</li>
  <li>Workers under 18 cannot opt out.</li>
</ul>

<h2>Rest between shifts</h2>
<p>Adult workers are entitled to <b>11 hours rest in a row</b> between working days. A close-then-open pattern, such as finishing at 23:00 and starting again at 07:00, breaks this rule.</p>

<h2>Weekly rest</h2>
<p>Adult workers are also entitled to an uninterrupted <b>24 hours without work each week</b>, or 48 hours each fortnight.</p>

<h2>Breaks during a shift</h2>
<p>Adults working <b>more than 6 hours</b> in a day are entitled to one uninterrupted <b>20-minute break</b> during the shift, not at the start or end. It does not have to be paid unless the contract says so.</p>

<h2>Young workers (under 18)</h2>
<p>Workers above school leaving age but under 18 have stronger protection:</p>
<ul>
  <li>no more than <b>8 hours a day</b> and <b>40 hours a week</b>, with no averaging and no opt-out;</li>
  <li><b>12 hours rest</b> between working days and <b>48 hours</b> rest each week;</li>
  <li>a <b>30-minute break</b> if they work more than 4.5 hours;</li>
  <li>generally no work between <b>10pm and 6am</b> (or 11pm and 7am if the contract says so). In some sectors, such as hotels and catering, retail and bakeries, they can work some of those hours, but generally not between midnight and 4am.</li>
</ul>

<h2>Night workers</h2>
<p>Someone who regularly works at least 3 hours during the night period (normally 11pm to 6am) is a night worker. Night workers should not work more than <b>8 hours in each 24</b> on average, and must be offered a free health assessment. They cannot opt out of the night work limit.</p>

<h2>Holiday</h2>
<p>Almost all workers are entitled to <b>5.6 weeks of paid holiday</b> a year. For someone working five days a week that is 28 days, which can include bank holidays. For irregular-hours and part-year workers, in leave years starting on or after 1 April 2024, holiday builds up at <b>12.07% of the hours worked</b> in each pay period.</p>

<h2>Keeping records</h2>
<p>You must keep records that show you are meeting the weekly limit and the night work limits, and keep them for two years. Copies of any opt-out agreements should be kept too.</p>

<h2>How ShiftFlow helps</h2>
<p>Checking every rota by hand is slow and easy to get wrong. <a href="../../shiftflow/">ShiftFlow</a> checks each rota before it is published, including 11 hours rest, the 48-hour average week, minimum breaks, limits for under-18s and visa hour caps, across every site. Errors block publishing, warnings are shown, and planned and actual hours are kept side by side for your records.</p>
""",
    },
    {
        "slug": "cyber-essentials-explained",
        "title": "Cyber Essentials explained: a plain-English guide for UK small businesses",
        "desc": "What Cyber Essentials and Cyber Essentials Plus are, the five technical controls, who needs "
                "certification and how a small business can prepare to pass first time.",
        "date": "2026-11-24", "minutes": 6, "topic": "Cyber security", "related": ("Cyber security", "services/cyber-security/"),
        "body": """
<p>Cyber Essentials is a UK government-backed scheme that helps organisations protect themselves against the most common online attacks. It is run by the National Cyber Security Centre (NCSC) and delivered by IASME through a network of certification bodies. For many small businesses it is the most sensible first step in cyber security, and more and more customers ask their suppliers for it.</p>

<h2>Cyber Essentials and Cyber Essentials Plus</h2>
<ul>
  <li><b>Cyber Essentials</b> is a self-assessment. You answer an online questionnaire about your IT, and a certification body reviews your answers.</li>
  <li><b>Cyber Essentials Plus</b> covers the same controls, but an assessor also checks them in person or remotely, for example by testing a sample of your devices. It has to be completed within three months of the basic certification.</li>
</ul>
<p>Certification lasts for 12 months, so you renew every year.</p>

<h2>The five controls</h2>
<ol>
  <li><b>Firewalls.</b> Every device and network connected to the internet is protected by a properly configured firewall.</li>
  <li><b>Secure configuration.</b> Default passwords are changed, unnecessary software and accounts are removed, and devices lock automatically.</li>
  <li><b>Security update management.</b> Software is supported by its maker and kept up to date. High-risk and critical updates must be installed within 14 days.</li>
  <li><b>User access control.</b> People only have the access they need, admin accounts are used only for admin tasks, and multi-factor authentication is switched on for cloud services.</li>
  <li><b>Malware protection.</b> Anti-malware software or application allow-listing protects every device in scope.</li>
</ol>

<h2>What is in scope</h2>
<p>Usually your whole organisation: office computers, laptops, phones and tablets that access company data, servers, network equipment and cloud services such as Microsoft 365. Home workers' devices, and personal devices used for work, are normally in scope too. You can certify only part of the organisation, but it must be clearly separated.</p>

<h2>Who needs it?</h2>
<p>Cyber Essentials is required for some UK central government contracts, particularly where personal information or certain ICT services are involved. Many larger businesses also ask their suppliers for it, and it gives you a clear, independent baseline to show customers and insurers.</p>

<h2>Common reasons businesses fail</h2>
<ul>
  <li>Unsupported software, such as computers still running an operating system the maker no longer updates.</li>
  <li>Multi-factor authentication missing on one or more cloud services.</li>
  <li>Updates not installed within 14 days.</li>
  <li>Staff using admin accounts for email and web browsing.</li>
  <li>Default passwords left on routers, firewalls or other devices.</li>
</ul>

<h2>How to prepare</h2>
<ol>
  <li>List every device, account and cloud service the business uses.</li>
  <li>Replace or upgrade anything that is out of support.</li>
  <li>Turn on multi-factor authentication for every cloud service.</li>
  <li>Set devices to update automatically, and check that they do.</li>
  <li>Remove admin rights from everyday accounts.</li>
  <li>Read the current question set from IASME before you start the assessment.</li>
</ol>

<h2>How BTree helps</h2>
<p>We help businesses <a href="../../services/cyber-security/">prepare for Cyber Essentials and Cyber Essentials Plus</a>: we review where you are today, fix the gaps in a sensible order and put the controls in place, so you can go into the assessment with confidence.</p>
<p class="note">Requirements are updated from time to time. Check the latest guidance on the <a href="https://www.ncsc.gov.uk/cyberessentials/overview" rel="noopener">NCSC website</a>.</p>
""",
    },
    {
        "slug": "microsoft-365-migration-checklist",
        "title": "Moving to Microsoft 365: a practical migration checklist",
        "desc": "A step-by-step checklist for moving a small or medium-sized business to Microsoft 365 from Google "
                "Workspace, another email provider or on-premises Exchange, without losing email.",
        "date": "2026-11-24", "minutes": 6, "topic": "Microsoft 365", "related": ("Microsoft 365 and Azure", "services/microsoft-365-azure/"),
        "body": """
<p>Moving email, calendars and files to Microsoft 365 is one of the most common IT projects for a growing business. Done well, staff barely notice. Done badly, email goes missing and nobody can find their files. This checklist covers the steps that make the difference.</p>

<h2>1. Take stock</h2>
<ul>
  <li>Every mailbox, including shared mailboxes such as info@ or accounts@.</li>
  <li>Aliases, distribution lists and forwarding rules.</li>
  <li>Calendars, contacts and any shared calendars or resources such as meeting rooms.</li>
  <li>Where files live today: a file server, Google Drive, Dropbox or individual laptops.</li>
  <li>Other systems that send email as your domain, such as your website, booking system or accounts software.</li>
</ul>

<h2>2. Choose the right licences</h2>
<p>Most businesses with up to 300 users use one of the Microsoft 365 Business plans. Business Premium adds device management with Intune and stronger identity and security controls. Shared mailboxes do not need a licence of their own in most cases, so do not buy more than you need.</p>

<h2>3. Tidy up before you move</h2>
<p>Close accounts for people who have left, archive or delete old data you do not need, and agree a simple folder structure for shared files. Migrating clutter makes the move slower and the result messier.</p>

<h2>4. Plan sign-in and security from day one</h2>
<ul>
  <li>Decide how people will sign in, and turn on multi-factor authentication for everyone.</li>
  <li>Make sure you have access to your domain's DNS settings, because you will need to change them.</li>
  <li>Set up SPF, DKIM and DMARC so your email is trusted and harder to spoof.</li>
</ul>

<h2>5. Choose the migration method</h2>
<ul>
  <li><b>From Google Workspace:</b> Microsoft provides a built-in migration for Gmail, calendars and contacts. Files in Google Drive are moved separately.</li>
  <li><b>From another provider:</b> an IMAP migration copies email, then calendars and contacts are exported and imported.</li>
  <li><b>From on-premises Exchange:</b> smaller organisations can move everything in one go; larger ones often use a hybrid set-up and move people in batches.</li>
</ul>

<h2>6. Move the data, then switch over</h2>
<ol>
  <li>A few days before, lower the time-to-live on your domain's MX record so the change takes effect quickly.</li>
  <li>Copy existing email and files while people keep working on the old system.</li>
  <li>At a planned time, usually outside working hours, point your MX record to Microsoft 365.</li>
  <li>Run a final copy to pick up anything that arrived during the switch.</li>
  <li>Set up Outlook, Teams and OneDrive on each device, and check that phones are connected.</li>
</ol>

<h2>7. After the move</h2>
<ul>
  <li>Keep the old system available, read-only, for a few weeks before you cancel it.</li>
  <li>Enrol devices in Intune if you have Business Premium, so they are kept secure and up to date.</li>
  <li>Show staff how to use Teams, SharePoint and OneDrive well. A short session saves weeks of confusion.</li>
</ul>

<h2>How BTree helps</h2>
<p>We plan and run <a href="../../services/microsoft-365-azure/">Microsoft 365 migrations</a> from Google Workspace, other providers and on-premises Exchange, with security set up properly from the start and minimal disruption for your team.</p>
""",
    },
]
