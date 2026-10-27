#!/usr/bin/env python3
"""Generate the You Can Sit With Us Foundation static site (shared header/footer)."""
import os, sys

OUT = sys.argv[1]

# ---- Site facts. Placeholders are in [brackets] until the founder supplies them. ----
EMAIL = "ach@sitwithusfoundation.com"
DONATE_URL = "https://www.zeffy.com/en-US/donation-form/summer-support-project"
SOCIALS = [("Instagram", "https://www.instagram.com/youcansitwithusfoundation/")]

NAV = [("index.html", "Home"), ("about.html", "About"), ("programs.html", "Programs"),
       ("get-involved.html", "Get Involved"), ("contact.html", "Contact")]

LOGO = """<svg class="bench" viewBox="0 0 64 48" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M14 4v22M50 4v22M14 6h36M14 12h36M14 18h36M8 26h48M5 31h54M10 31v14M54 31v14M14 31v9M50 31v9"/></svg><span class="wordmark"><span class="wm-top">You Can Sit</span><span class="wm-mid">With Us</span><span class="wm-bot">Foundation</span></span>"""


def SEAL(uid, cls="seal"):
    return f"""<svg class="{cls}" viewBox="0 0 600 600" role="img" aria-label="You Can Sit With Us Foundation seal">
<defs><path id="st-{uid}" d="M 88 300 A 212 212 0 0 1 512 300"/><path id="sb-{uid}" d="M 62 300 A 238 238 0 0 0 538 300"/></defs>
<circle cx="300" cy="300" r="262" fill="none" stroke="currentColor" stroke-width="3"/>
<circle cx="300" cy="300" r="250" fill="none" stroke="var(--seal-accent)" stroke-width="1.5"/>
<circle cx="300" cy="300" r="196" fill="none" stroke="var(--seal-accent)" stroke-width="1.5"/>
<text fill="currentColor" font-size="34" font-weight="600" letter-spacing="7"><textPath href="#st-{uid}" startOffset="50%" text-anchor="middle">YOU CAN SIT WITH US</textPath></text>
<text fill="currentColor" font-size="22" font-weight="500" letter-spacing="14"><textPath href="#sb-{uid}" startOffset="50%" text-anchor="middle">FOUNDATION</textPath></text>
<circle cx="66" cy="300" r="5" fill="var(--seal-accent)"/><circle cx="534" cy="300" r="5" fill="var(--seal-accent)"/>
<g transform="translate(204 228) scale(3)" fill="none" stroke="var(--seal-accent)" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4v22M50 4v22M14 6h36M14 12h36M14 18h36M8 26h48M5 31h54M10 31v14M54 31v14M14 31v9M50 31v9"/></g>
</svg>"""


def page(fname, title, desc, body):
    links = "\n".join(
        f'        <a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV)
    socials = " ".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIALS)
    full_title = "You Can Sit With Us Foundation" if fname == "index.html" else f"{title} | You Can Sit With Us"
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="images/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="images/apple-touch-icon.png">
<meta property="og:image" content="https://skinny479.github.io/you-can-sit-with-us/images/og-image.png">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <div class="wrap nav-row">
    <a class="brand" href="index.html" aria-label="You Can Sit With Us Foundation home">{LOGO}</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">
      <svg width="22" height="22" viewBox="0 0 22 22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h16M3 11h16M3 16h16"/></svg>
    </button>
    <nav class="links" id="site-nav" aria-label="Main">
{links}
        <a class="btn btn-coral nav-donate" href="donate.html">Donate</a>
    </nav>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="site">
  <div class="wrap footer-grid">
    <div>
      <a class="brand-seal" href="index.html" aria-label="You Can Sit With Us Foundation home">{SEAL("foot", "seal seal-foot")}</a>
      <p class="muted">Because everyone deserves a seat at the table.</p>
    </div>
    <div class="footer-col">
      <h2>Explore</h2>
      <a href="about.html">About</a><a href="programs.html">Programs</a><a href="get-involved.html">Get Involved</a><a href="donate.html">Donate</a>
    </div>
    <div class="footer-col">
      <h2>Connect</h2>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <p>{socials}</p>
      <p class="muted">Springdale, Arkansas</p>
    </div>
  </div>
  <div class="wrap legal">
    <p>&copy; <span id="year">2026</span> You Can Sit with Us Foundation, an Arkansas nonprofit corporation and 501(c)(3) public charity, EIN 42-2597781. Donations are tax-deductible to the extent allowed by law.</p>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)


DONATE_BTN = f'<a class="btn btn-coral" href="{DONATE_URL}" target="_blank" rel="noopener">Donate on Zeffy</a>'

# ---------------- Home ----------------
page("index.html", "Home",
     "The You Can Sit With Us Foundation, founded by Anna Claire Hay, is a Northwest Arkansas nonprofit built on a simple message of inclusion. Everyone deserves a seat at the table.",
f"""  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="eyebrow">Northwest Arkansas &middot; 501(c)(3) nonprofit</p>
        <h1>Everyone deserves a seat at the table.</h1>
        <p class="lead">The You Can Sit With Us Foundation started as a simple message of inclusion. Today we show up for Northwest Arkansas kids with school supplies, free meals, and a clear message: you belong here.</p>
        <div class="actions">
          <a class="btn btn-coral" href="donate.html">Give today</a>
          <a class="btn btn-ghost" href="get-involved.html">Get involved</a>
        </div>
      </div>
      <figure class="hero-photo">
        <img src="images/founder-shirt.jpg" alt="Founder Anna Claire Hay wearing a You Can Sit With Us t-shirt" width="800" height="1339">
      </figure>
    </div>
  </section>

  <section class="symbol">
    <div class="wrap narrow symbol-inner">
      {SEAL("sym", "seal seal-sym")}
      <p class="eyebrow">Our symbol</p>
      <h2>There&rsquo;s always room on the bench.</h2>
      <!-- TODO: founder to confirm or rewrite the meaning of the bench -->
      <p>A bench is built to be shared. Scoot over, and there&rsquo;s room for one more. That&rsquo;s the whole idea behind You Can Sit With Us: no one should have to sit alone, at lunch, on the playground, or anywhere else.</p>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">What we do</p>
        <h2>Small acts that say &ldquo;you belong.&rdquo;</h2>
      </div>
      <div class="cards">
        <article class="card">
          <h3>Back-to-school backpacks</h3>
          <p>We send students into the new school year with backpacks filled with school supplies and essential items.</p>
        </article>
        <article class="card">
          <h3>Free family meals</h3>
          <p>Our events serve free hot meals so families can gather, eat, and connect.</p>
        </article>
        <article class="card">
          <h3>A message of inclusion</h3>
          <p>Everything we do comes back to one idea: every kid deserves a place where they're welcome.</p>
        </article>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap narrow">
      <p class="eyebrow">Signature event</p>
      <h2>The Summer of Support Project</h2>
      <p>Our Summer of Support event filled the Jones Center in Springdale with backpacks of school supplies, free meals, bounce houses, snow cones, and community resource vendors for local families.</p>
      <div class="stats">
        <div><strong>600</strong><span>meals served</span></div>
        <div><strong>200</strong><span>backpacks given out</span></div>
      </div>
      <blockquote>&ldquo;Every child deserves to start the school year feeling prepared, confident, and supported.&rdquo;<cite>Anna Claire Hay, Founder</cite></blockquote>
      <p><a class="text-link" href="programs.html">See our programs &rarr;</a></p>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">In the community</p>
        <h2>Saving seats all over Northwest Arkansas.</h2>
      </div>
      <div class="gallery">
        <figure class="g-wide"><img src="images/school-visit.jpg" alt="Anna Claire Hay with a class of elementary students" loading="lazy" width="1100" height="558"><figcaption>Visiting students in the classroom</figcaption></figure>
        <figure><img src="images/community-gathering.jpg" alt="Kids and volunteers gathered together on yoga mats" loading="lazy" width="690" height="715"><figcaption>Kids and volunteers together</figcaption></figure>
        <figure><img src="images/volunteers.jpg" alt="A large group of volunteers in matching shirts" loading="lazy" width="1100" height="1201"><figcaption>Volunteers ready to serve</figcaption></figure>
        <figure><img class="pos-bottom" src="images/adopt-a-highway.jpg" alt="Anna Claire Hay beside her Adopt a Highway litter control sign" loading="lazy" width="800" height="1220"><figcaption>Anna Claire&rsquo;s Adopt a Highway cleanup</figcaption></figure>
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap cta-inner">
      <svg class="bench-cta" viewBox="0 0 64 48" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M14 4v22M50 4v22M14 6h36M14 12h36M14 18h36M8 26h48M5 31h54M10 31v14M54 31v14M14 31v9M50 31v9"/></svg>
      <h2>Help us save a seat for every kid.</h2>
      <p>Your gift puts school supplies, meals, and support in the hands of Northwest Arkansas kids.</p>
      <a class="btn btn-gold" href="donate.html">Donate</a>
    </div>
  </section>""")

# ---------------- About ----------------
page("about.html", "About",
     "Learn how the You Can Sit With Us Foundation grew from a simple message of inclusion into a 501(c)(3) nonprofit in Northwest Arkansas.",
"""  <section class="page-hero">
    <div class="wrap narrow">
      <p class="eyebrow">About us</p>
      <h1>From a message to a mission.</h1>
      <p class="lead">What started as a simple message of inclusion has grown into something much bigger.</p>
    </div>
  </section>

  <section>
    <div class="wrap narrow prose">
      <h2>Our story</h2>
      <figure class="float-photo">
        <img src="images/founder-childhood.jpg" alt="A young Anna Claire Hay holding a Sweet Times photo from the Juanita Brown Memorial" width="700" height="1112">
        <figcaption>A young Anna Claire with a &ldquo;Sweet Times&rdquo; photo from the Juanita Brown Memorial.</figcaption>
      </figure>
      <p>You Can Sit With Us began with an idea every kid understands: it matters who saves you a seat. Anna Claire Hay has carried that message for years, and her work through You Can Sit With Us earned her recognition as Arkansas&rsquo;s Top Youth Volunteer. Today the You Can Sit With Us Foundation is a 501(c)(3) nonprofit organization.</p>
      <p>As a nonprofit, the foundation keeps growing its impact. The Summer of Support Project gave students in Springdale backpacks filled with school supplies and essential items, alongside free meals and a night of family fun, with support from Tyson Foods, Sam&rsquo;s Club, Office Depot, and other community partners.</p>

      <h2>Our mission</h2>
      <!-- TODO: replace with the founder's official mission statement -->
      <p class="mission">To make sure every child in our community knows they belong, by meeting practical needs and spreading a message of inclusion.</p>

      <h2>What we believe</h2>
      <ul class="values">
        <li><strong>Everyone gets a seat.</strong> No kid should feel left out.</li>
        <li><strong>Practical help matters.</strong> A full backpack and a hot meal say &ldquo;we see you&rdquo; louder than words.</li>
        <li><strong>Community makes it possible.</strong> Every event happens because neighbors show up.</li>
      </ul>

      <h2>Meet our founder</h2>
      <div class="founder">
        <img class="founder-img" src="images/founder-book.jpg" alt="Anna Claire Hay holding her children's book You Can Sit With Jackson" width="690" height="903">
        <div>
          <p><strong>Anna Claire Hay</strong> is a proud native of Northwest Arkansas currently residing in Fayetteville. A graduate of the University of Arkansas and recent applicant to the University of Arkansas for Medical Sciences, Anna Claire is pursuing her lifelong dream of becoming Dr. Anna Claire Hay. She is the daughter of Greg and Kelly Brown of Springdale, Arkansas and John Hay of Houston, Texas.</p>
          <p>Passionate about growth and challenge, Anna Claire recently completed her first half marathon and enjoys spending time with her Bernedoodle, Ace. A true Arkansas girl at heart, she loves Razorback baseball, DIY home projects, reading, and spending time on the lake.</p>
        </div>
      </div>
      <p>Beyond the crown, Anna Claire has dedicated her life to serving others across the state of Arkansas. In 2019, she was honored as Arkansas&rsquo;s Top Youth Volunteer for her work through her nonprofit organization, You Can Sit With Us, a 501(c)(3) focused on inclusion, kindness, and community impact. She is also a published author of the children&rsquo;s book <em>You Can Sit With Jackson</em>, created to encourage kindness, acceptance, and inclusion among young students. In recognition of her commitment to service, Anna Claire has also been named a recipient of the President&rsquo;s Volunteer Service Award Gold Award.</p>
      <p>While attending the University of Arkansas, she was a member of Kappa Delta, where she served on the leadership team.</p>
      <p>Anna Claire&rsquo;s career in fashion and pageantry has taken her around the world, modeling for recognized designers including Ashley Lauren and Robin Towle Designs, with appearances spanning from Atlanta to Paris, France.</p>

      <div class="honors">
        <div><strong>Miss Arkansas USA</strong><span>2026</span></div>
        <div><strong>Arkansas&rsquo;s Top Youth Volunteer</strong><span>2019</span></div>
        <div><strong>President&rsquo;s Volunteer Service Award</strong><span>Gold</span></div>
        <div><strong>Published author</strong><span><em>You Can Sit With Jackson</em></span></div>
      </div>

      <blockquote>&ldquo;Every child deserves to start the school year feeling prepared, confident, and supported.&rdquo;<cite>Anna Claire Hay</cite></blockquote>
    </div>
  </section>""")

# ---------------- Programs ----------------
page("programs.html", "Programs",
     "The Summer of Support Project and other You Can Sit With Us Foundation programs serving children in Northwest Arkansas.",
f"""  <section class="page-hero">
    <div class="wrap narrow">
      <p class="eyebrow">Programs</p>
      <h1>Showing up for local kids.</h1>
      <p class="lead">Our programs meet real needs and remind every child they have a place at the table.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <article class="program">
        <div class="program-meta">
          <span class="tag">Flagship event</span>
          <p><strong>Back-to-school season</strong><br>The Jones Center, Springdale</p>
        </div>
        <div>
          <h2>Summer of Support Project</h2>
          <p>Held just before back-to-school, Summer of Support sends students into the new year ready to learn. Students received backpacks filled with school supplies and essential items, and families enjoyed:</p>
          <ul class="checks">
            <li>Free meals provided by Tyson Foods</li>
            <li>Bounce houses and a snow cone stand</li>
            <li>Family-friendly activities</li>
            <li>Community resource vendors</li>
          </ul>
          <div class="stats">
            <div><strong>600</strong><span>meals served</span></div>
            <div><strong>200</strong><span>backpacks given out</span></div>
          </div>
          <p class="muted">With support from Tyson Foods, Sam&rsquo;s Club, Office Depot, and other partners.</p>
          <div class="actions">{DONATE_BTN}</div>
        </div>
      </article>

      <article class="program program-soon">
        <div class="program-meta">
          <span class="tag tag-soft">Coming soon</span>
        </div>
        <div>
          <h2>What's next</h2>
          <p>We're planning our next chapter. Follow us or reach out to hear about upcoming events and ways to help.</p>
          <p><a class="text-link" href="contact.html">Stay in touch &rarr;</a></p>
        </div>
      </article>
    </div>
  </section>""")

# ---------------- Get Involved ----------------
page("get-involved.html", "Get Involved",
     "Volunteer, donate supplies, partner with us, or spread the word to help the You Can Sit With Us Foundation serve local kids.",
f"""  <section class="page-hero">
    <div class="wrap narrow">
      <p class="eyebrow">Get involved</p>
      <h1>Pull up a chair and help.</h1>
      <p class="lead">There are lots of ways to make sure every kid has a seat at the table.</p>
    </div>
  </section>

  <section>
    <div class="wrap cards">
      <article class="card">
        <h3>Volunteer at an event</h3>
        <p>Pack backpacks, serve meals, and welcome families at our events.</p>
        <a class="text-link" href="mailto:{EMAIL}?subject=Volunteer">Email us to volunteer &rarr;</a>
      </article>
      <article class="card">
        <h3>Donate supplies</h3>
        <p>Help fill backpacks with school supplies and essentials. Contact us for our current list of needed items.</p>
        <a class="text-link" href="mailto:{EMAIL}?subject=Supply%20donation">Ask what's needed &rarr;</a>
      </article>
      <article class="card">
        <h3>Partner with us</h3>
        <p>Businesses, schools, churches, and community groups can sponsor an event or host a supply drive.</p>
        <a class="text-link" href="mailto:{EMAIL}?subject=Partnership">Start a conversation &rarr;</a>
      </article>
      <article class="card">
        <h3>Spread the word</h3>
        <p>Follow us, share our posts, and tell a friend. Every share helps another kid find their seat.</p>
        <a class="text-link" href="contact.html">Find us online &rarr;</a>
      </article>
    </div>
  </section>

  <section class="cta">
    <div class="wrap cta-inner">
      <svg class="bench-cta" viewBox="0 0 64 48" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M14 4v22M50 4v22M14 6h36M14 12h36M14 18h36M8 26h48M5 31h54M10 31v14M54 31v14M14 31v9M50 31v9"/></svg>
      <h2>Prefer to give?</h2>
      <p>Your gift goes toward school supplies, meals, and support for local children.</p>
      <a class="btn btn-gold" href="donate.html">Donate</a>
    </div>
  </section>""")

# ---------------- Donate ----------------
page("donate.html", "Donate",
     "Donate to the You Can Sit With Us Foundation to provide school supplies, meals, and support for children in Northwest Arkansas.",
f"""  <section class="page-hero">
    <div class="wrap narrow">
      <p class="eyebrow">Donate</p>
      <h1>Save a seat for a kid who needs one.</h1>
      <p class="lead">Your gift provides backpacks of school supplies, meals, and support for children in our community.</p>
    </div>
  </section>

  <section>
    <div class="wrap narrow">
      <div class="donate-panel">
        <h2>Give securely through Zeffy</h2>
        <p>Zeffy is a free fundraising platform, so 100% of your donation reaches the foundation.</p>
        {DONATE_BTN}
        <p class="muted small">You Can Sit with Us Foundation is an Arkansas nonprofit corporation and 501(c)(3) public charity, EIN 42-2597781. Donations are tax-deductible to the extent allowed by law.</p>
      </div>

      <div class="prose">
        <h2>Other ways to give</h2>
        <ul class="values">
          <li><strong>Supplies.</strong> Donate school supplies and essentials for student backpacks. <a href="mailto:{EMAIL}?subject=Supply%20donation">Email us</a> for the current list.</li>
          <li><strong>Sponsorship.</strong> Businesses can sponsor an event. <a href="mailto:{EMAIL}?subject=Sponsorship">Let's talk</a>.</li>
          <li><strong>Employer matching.</strong> Many employers match gifts. Ask your HR team.</li>
        </ul>
      </div>
    </div>
  </section>""")

# ---------------- Contact ----------------
socials_list = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">@youcansitwithusfoundation</a> on {n}</li>' for n, u in SOCIALS)
page("contact.html", "Contact",
     "Contact the You Can Sit With Us Foundation in Springdale, Arkansas.",
f"""  <section class="page-hero">
    <div class="wrap narrow">
      <p class="eyebrow">Contact</p>
      <h1>We'd love to hear from you.</h1>
      <p class="lead">Questions, ideas, volunteering, or partnerships: reach out anytime.</p>
    </div>
  </section>

  <section>
    <div class="wrap narrow contact-grid">
      <div class="card">
        <h3>Email</h3>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div class="card">
        <h3>Follow us</h3>
        <ul class="plain">{socials_list}</ul>
      </div>
      <div class="card">
        <h3>Where we serve</h3>
        <p>Springdale and Northwest Arkansas</p>
      </div>
    </div>
  </section>""")

# ---------------- 404 ----------------
page("404.html", "Page not found", "Page not found.",
"""  <section class="page-hero">
    <div class="wrap narrow">
      <p class="eyebrow">404</p>
      <svg class="bench-lg" viewBox="0 0 64 48" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M14 4v22M50 4v22M14 6h36M14 12h36M14 18h36M8 26h48M5 31h54M10 31v14M54 31v14M14 31v9M50 31v9"/></svg>
      <h1>This seat is empty.</h1>
      <p class="lead">We couldn't find that page, but there's still room for you.</p>
      <p><a class="btn btn-coral" href="index.html">Back to home</a></p>
    </div>
  </section>""")

print("built")
