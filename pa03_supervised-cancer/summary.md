Basically, this paper is demonstrating a novel new method they developed that uses microRNA in the bloodstream to try and detect cancer as an easier and cheaper method, which should help improve early screening for breast cancer.

Based on previous research, breast cancer cells seem to have specific miRNA (micro RNA) in their bloodstream.

The data for this study was gotten from breast cancer patients and patients with benign tumors, and they excluded people on medication or with other serious cancers in other organs. They collected samples from people 60 years or older volunteers from Toray Industries and samples from the National Center for Geriatrics and Gerontology Biobank, and female volunteers from the Yokohama Minoru Clinic in 2015. Also, patients with other types of cancers were included so they could narrow down the type of cancer to just breast cancer.

The RNA was extracted, then special methods were used to detect and find miRNA. The data was validated using quantitative RT-PCR analysis, alongside other methods to ensure the data was all good.

Once the data from the RNA was extracted, they seperated the DNA into training and test cohorts, and used a P value < .01 to determine statistical significance. Filtering for robust biomarkers, they then used a thing called Fisher's linear discriminant analysis to calculate sensitivity, specificity and accuracy for training / testing. They used a t-test to evaluate the results, and then used Pearson's correlation analysis to see the correlations between the results. They used R as a programming language.

They had a fairly small training cohort and a pretty big test cohort. The training results were mid, but the test results were pretty good. They got a high AUC of .971.

Cancer screening for older women is pretty low in Japan, so having a cheap and more painless method is really important to improve screenings. Since this technique is simpler and less invasive, it may be a good option. They found 5 miRNA that seem pretty good and dont have any problems. Any differences between the samples should have been normalized, so there shouldn't be a problem with it. This method can't distinguish benign and malignant tumors, so it should only be use for initial screening.