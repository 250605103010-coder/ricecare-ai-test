# Advanced data for RiceCare AI portals

Every row has a `data_label`. Show that label (or a clear badge) wherever the data appears in the app.

| File | Used by | data_label | Real or not |
|---|---|---|---|
| treatment_options.csv | Agro Solutions (chemical, biological, natural, traditional, cultural kept separate) | GENERAL_KNOWLEDGE_UNVERIFIED | Widely published guidance, **not checked by an expert**. No doses, brands or prices |
| nutrient_issues.csv | Farmer / Agro (fertilizer and nutrients) | GENERAL_KNOWLEDGE_UNVERIFIED | General symptoms. No amounts, soil test needed |
| growth_stages.csv | Farmer (crop records) | GENERAL_KNOWLEDGE_UNVERIFIED | Stage names only, no day counts |
| government_schemes.csv | Agro Solutions | GENERAL_KNOWLEDGE_UNVERIFIED | Scheme names only. No amounts or eligibility. **Check the official site** |
| research_resources.csv | Research | REAL_PUBLIC_RESOURCE_LINK_CHECK_BEFORE_PUBLISHING | Real public databases. Open each link once before showing it |
| suppliers_sample.csv, products_sample.csv | Agro Solutions | SAMPLE_NOT_REAL | **Fictional.** Not real businesses, no prices, no registrations |
| experts_sample.csv, questions_sample.csv | Community | SAMPLE_NOT_REAL | **Fictional** placeholders |
| field_records_synthetic.csv, expenses_synthetic.csv | Farmer (records, expenses) | SYNTHETIC | Made-up rows to test the interface only |

Rules kept in these files:
- Treatment rows name active ingredients as "commonly referenced", never as a prescription. The app must not suggest a treatment automatically from an AI result.
- Nothing here is a real observation, review, price or registration.
- Replace SAMPLE and SYNTHETIC rows with real, verified records before any public release.

Check the files: `python data/advanced/validate_advanced_data.py`
