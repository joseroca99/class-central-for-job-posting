"""clonesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='index'),

    path('about',AboutView.as_view(), name='about'),
    path('about/careers',AboutCareersView.as_view(), name='about-careers'),
    path('about/privacy-policy',AboutPrivacyPolicyView.as_view(), name='about-privacy-policy'),
    path('collection/ivy-league-moocs',CollectionIvyLeagueMoocsView.as_view(), name='collection-ivy-league-moocs'),
    path('collection/top-free-online-courses',CollectionTopFreeOnlineCoursesView.as_view(), name='collection-top-free-online-courses'),
    path('collections',CollectionsView.as_view(), name='collections'),
    path('contact',ContactView.as_view(), name='contact'),
    path('course/edx-unlocking-information-security-part-i-16964',CourseEdxUnlockingInformationSecurityPartI16964View.as_view(), name='course-edx-unlocking-information-security-part-i-16964'),
    path('course/intro-indoor-air-quality-9706',CourseIntroIndoorAirQuality9706View.as_view(), name='course-intro-indoor-air-quality-9706'),
    path('course/social-innovation-6655',CourseSocialInnovation6655View.as_view(), name='course-social-innovation-6655'),
    path('help',HelpView.as_view(), name='help'),
    path('help/moocs',HelpMoocsView.as_view(), name='help-moocs'),
    path('institution/amazon',InstitutionAmazonView.as_view(), name='institution-amazon'),
    path('institution/british-council',InstitutionBritishCouncilView.as_view(), name='institution-british-council'),
    path('institution/google',InstitutionGoogleView.as_view(), name='institution-google'),
    path('institution/ibm',InstitutionIbmView.as_view(), name='institution-ibm'),
    path('institution/linuxfoundation',InstitutionLinuxfoundationView.as_view(), name='institution-linuxfoundation'),
    path('institution/microsoft',InstitutionMicrosoftView.as_view(), name='institution-microsoft'),
    path('institution/salesforce',InstitutionSalesforceView.as_view(), name='institution-salesforce'),
    path('institution/smithsonian',InstitutionSmithsonianView.as_view(), name='institution-smithsonian'),
    path('institution/united-nations',InstitutionUnitedNationsView.as_view(), name='institution-united-nations'),
    path('institutions',InstitutionsView.as_view(), name='institutions'),
    path('lists',ListsView.as_view(), name='lists'),
    path('login',LoginView.as_view(), name='login'),
    path('most-popular-courses',MostPopularCoursesView.as_view(), name='most-popular-courses'),
    path('new-online-courses',NewOnlineCoursesView.as_view(), name='new-online-courses'),
    path('provider/coursera',ProviderCourseraView.as_view(), name='provider-coursera'),
    path('provider/edx',ProviderEdxView.as_view(), name='provider-edx'),
    path('provider/futurelearn',ProviderFuturelearnView.as_view(), name='provider-futurelearn'),
    path('provider/linkedin-learning',ProviderLinkedinLearningView.as_view(), name='provider-linkedin-learning'),
    path('provider/skillshare',ProviderSkillshareView.as_view(), name='provider-skillshare'),
    path('provider/swayam',ProviderSwayamView.as_view(), name='provider-swayam'),
    path('provider/udacity',ProviderUdacityView.as_view(), name='provider-udacity'),
    path('provider/udemy',ProviderUdemyView.as_view(), name='provider-udemy'),
    path('providers',ProvidersView.as_view(), name='providers'),
    path('rankings',RankingsView.as_view(), name='rankings'),
    path('report/',ReportView.as_view(), name='report-'),
    path('signup',SignupView.as_view(), name='signup'),
    path('starting-this-month',StartingThisMonthView.as_view(), name='starting-this-month'),
    path('subject/accounting',SubjectAccountingView.as_view(), name='subject-accounting'),
    path('subject/aerospace-engineering',SubjectAerospaceEngineeringView.as_view(), name='subject-aerospace-engineering'),
    path('subject/agriculture',SubjectAgricultureView.as_view(), name='subject-agriculture'),
    path('subject/ai',SubjectAiView.as_view(), name='subject-ai'),
    path('subject/algebra',SubjectAlgebraView.as_view(), name='subject-algebra'),
    path('subject/algorithms-and-data-structures',SubjectAlgorithmsAndDataStructuresView.as_view(), name='subject-algorithms-and-data-structures'),
    path('subject/anatomy',SubjectAnatomyView.as_view(), name='subject-anatomy'),
    path('subject/anthropology',SubjectAnthropologyView.as_view(), name='subject-anthropology'),
    path('subject/applied-science',SubjectAppliedScienceView.as_view(), name='subject-applied-science'),
    path('subject/archaeology',SubjectArchaeologyView.as_view(), name='subject-archaeology'),
    path('subject/art-and-design',SubjectArtAndDesignView.as_view(), name='subject-art-and-design'),
    path('subject/astronomy',SubjectAstronomyView.as_view(), name='subject-astronomy'),
    path('subject/big-data',SubjectBigDataView.as_view(), name='subject-big-data'),
    path('subject/bim',SubjectBimView.as_view(), name='subject-bim'),
    path('subject/bioinformatics',SubjectBioinformaticsView.as_view(), name='subject-bioinformatics'),
    path('subject/biology',SubjectBiologyView.as_view(), name='subject-biology'),
    path('subject/blockchain',SubjectBlockchainView.as_view(), name='subject-blockchain'),
    path('subject/blue-team',SubjectBlueTeamView.as_view(), name='subject-blue-team'),
    path('subject/business',SubjectBusinessView.as_view(), name='subject-business'),
    path('subject/business-intelligence',SubjectBusinessIntelligenceView.as_view(), name='subject-business-intelligence'),
    path('subject/business-software',SubjectBusinessSoftwareView.as_view(), name='subject-business-software'),
    path('subject/cad',SubjectCadView.as_view(), name='subject-cad'),
    path('subject/calculus',SubjectCalculusView.as_view(), name='subject-calculus'),
    path('subject/career-development',SubjectCareerDevelopmentView.as_view(), name='subject-career-development'),
    path('subject/chemical-engineering',SubjectChemicalEngineeringView.as_view(), name='subject-chemical-engineering'),
    path('subject/chemistry',SubjectChemistryView.as_view(), name='subject-chemistry'),
    path('subject/childhood-development',SubjectChildhoodDevelopmentView.as_view(), name='subject-childhood-development'),
    path('subject/civil-engineering',SubjectCivilEngineeringView.as_view(), name='subject-civil-engineering'),
    path('subject/cloud-computing',SubjectCloudComputingView.as_view(), name='subject-cloud-computing'),
    path('subject/cme',SubjectCmeView.as_view(), name='subject-cme'),
    path('subject/combinatorics',SubjectCombinatoricsView.as_view(), name='subject-combinatorics'),
    path('subject/communication-skills',SubjectCommunicationSkillsView.as_view(), name='subject-communication-skills'),
    path('subject/computer-graphics',SubjectComputerGraphicsView.as_view(), name='subject-computer-graphics'),
    path('subject/computer-networking',SubjectComputerNetworkingView.as_view(), name='subject-computer-networking'),
    path('subject/course-development',SubjectCourseDevelopmentView.as_view(), name='subject-course-development'),
    path('subject/crisis-management',SubjectCrisisManagementView.as_view(), name='subject-crisis-management'),
    path('subject/cryptography',SubjectCryptographyView.as_view(), name='subject-cryptography'),
    path('subject/cs',SubjectCsView.as_view(), name='subject-cs'),
    path('subject/csr',SubjectCsrView.as_view(), name='subject-csr'),
    path('subject/culture',SubjectCultureView.as_view(), name='subject-culture'),
    path('subject/customer-service',SubjectCustomerServiceView.as_view(), name='subject-customer-service'),
    path('subject/cybersecurity',SubjectCybersecurityView.as_view(), name='subject-cybersecurity'),
    path('subject/data-analysis',SubjectDataAnalysisView.as_view(), name='subject-data-analysis'),
    path('subject/data-mining',SubjectDataMiningView.as_view(), name='subject-data-mining'),
    path('subject/data-science',SubjectDataScienceView.as_view(), name='subject-data-science'),
    path('subject/data-visualization',SubjectDataVisualizationView.as_view(), name='subject-data-visualization'),
    path('subject/databases',SubjectDatabasesView.as_view(), name='subject-databases'),
    path('subject/deep-learning',SubjectDeepLearningView.as_view(), name='subject-deep-learning'),
    path('subject/design-and-creativity',SubjectDesignAndCreativityView.as_view(), name='subject-design-and-creativity'),
    path('subject/design-thinking',SubjectDesignThinkingView.as_view(), name='subject-design-thinking'),
    path('subject/devops',SubjectDevopsView.as_view(), name='subject-devops'),
    path('subject/devsecops',SubjectDevsecopsView.as_view(), name='subject-devsecops'),
    path('subject/digital-forensics',SubjectDigitalForensicsView.as_view(), name='subject-digital-forensics'),
    path('subject/digital-media',SubjectDigitalMediaView.as_view(), name='subject-digital-media'),
    path('subject/discrete-mathematics',SubjectDiscreteMathematicsView.as_view(), name='subject-discrete-mathematics'),
    path('subject/disease-and-disorders',SubjectDiseaseAndDisordersView.as_view(), name='subject-disease-and-disorders'),
    path('subject/distributed-systems',SubjectDistributedSystemsView.as_view(), name='subject-distributed-systems'),
    path('subject/earth-science',SubjectEarthScienceView.as_view(), name='subject-earth-science'),
    path('subject/economics',SubjectEconomicsView.as_view(), name='subject-economics'),
    path('subject/education',SubjectEducationView.as_view(), name='subject-education'),
    path('subject/electrical-engineering',SubjectElectricalEngineeringView.as_view(), name='subject-electrical-engineering'),
    path('subject/energy-systems',SubjectEnergySystemsView.as_view(), name='subject-energy-systems'),
    path('subject/engineering',SubjectEngineeringView.as_view(), name='subject-engineering'),
    path('subject/entrepreneurship',SubjectEntrepreneurshipView.as_view(), name='subject-entrepreneurship'),
    path('subject/environmental-science',SubjectEnvironmentalScienceView.as_view(), name='subject-environmental-science'),
    path('subject/esl',SubjectEslView.as_view(), name='subject-esl'),
    path('subject/ethical-hacking',SubjectEthicalHackingView.as_view(), name='subject-ethical-hacking'),
    path('subject/ethics',SubjectEthicsView.as_view(), name='subject-ethics'),
    path('subject/finance',SubjectFinanceView.as_view(), name='subject-finance'),
    path('subject/food',SubjectFoodView.as_view(), name='subject-food'),
    path('subject/forensic-science',SubjectForensicScienceView.as_view(), name='subject-forensic-science'),
    path('subject/foundations-of-mathematics',SubjectFoundationsOfMathematicsView.as_view(), name='subject-foundations-of-mathematics'),
    path('subject/game-development',SubjectGameDevelopmentView.as_view(), name='subject-game-development'),
    path('subject/geometry',SubjectGeometryView.as_view(), name='subject-geometry'),
    path('subject/gis',SubjectGisView.as_view(), name='subject-gis'),
    path('subject/governance',SubjectGovernanceView.as_view(), name='subject-governance'),
    path('subject/grammar-writing',SubjectGrammarWritingView.as_view(), name='subject-grammar-writing'),
    path('subject/hci',SubjectHciView.as_view(), name='subject-hci'),
    path('subject/health',SubjectHealthView.as_view(), name='subject-health'),
    path('subject/health-care',SubjectHealthCareView.as_view(), name='subject-health-care'),
    path('subject/higher-education',SubjectHigherEducationView.as_view(), name='subject-higher-education'),
    path('subject/history',SubjectHistoryView.as_view(), name='subject-history'),
    path('subject/human-resources',SubjectHumanResourcesView.as_view(), name='subject-human-resources'),
    path('subject/human-rights',SubjectHumanRightsView.as_view(), name='subject-human-rights'),
    path('subject/humanities',SubjectHumanitiesView.as_view(), name='subject-humanities'),
    path('subject/industry-specific',SubjectIndustrySpecificView.as_view(), name='subject-industry-specific'),
    path('subject/information-technology',SubjectInformationTechnologyView.as_view(), name='subject-information-technology'),
    path('subject/infosec',SubjectInfosecView.as_view(), name='subject-infosec'),
    path('subject/infosec-certifications',SubjectInfosecCertificationsView.as_view(), name='subject-infosec-certifications'),
    path('subject/innovation',SubjectInnovationView.as_view(), name='subject-innovation'),
    path('subject/internet-of-things',SubjectInternetOfThingsView.as_view(), name='subject-internet-of-things'),
    path('subject/journalism',SubjectJournalismView.as_view(), name='subject-journalism'),
    path('subject/jupyter',SubjectJupyterView.as_view(), name='subject-jupyter'),
    path('subject/k12',SubjectK12View.as_view(), name='subject-k12'),
    path('subject/language-learning',SubjectLanguageLearningView.as_view(), name='subject-language-learning'),
    path('subject/law',SubjectLawView.as_view(), name='subject-law'),
    path('subject/library-science',SubjectLibraryScienceView.as_view(), name='subject-library-science'),
    path('subject/linear-programming',SubjectLinearProgrammingView.as_view(), name='subject-linear-programming'),
    path('subject/linguistics',SubjectLinguisticsView.as_view(), name='subject-linguistics'),
    path('subject/literature',SubjectLiteratureView.as_view(), name='subject-literature'),
    path('subject/machine-learning',SubjectMachineLearningView.as_view(), name='subject-machine-learning'),
    path('subject/malware-analysis',SubjectMalwareAnalysisView.as_view(), name='subject-malware-analysis'),
    path('subject/management-and-leadership',SubjectManagementAndLeadershipView.as_view(), name='subject-management-and-leadership'),
    path('subject/manufacturing',SubjectManufacturingView.as_view(), name='subject-manufacturing'),
    path('subject/marketing',SubjectMarketingView.as_view(), name='subject-marketing'),
    path('subject/materials-science',SubjectMaterialsScienceView.as_view(), name='subject-materials-science'),
    path('subject/mathematical-logic',SubjectMathematicalLogicView.as_view(), name='subject-mathematical-logic'),
    path('subject/maths',SubjectMathsView.as_view(), name='subject-maths'),
    path('subject/mechanical-engineering',SubjectMechanicalEngineeringView.as_view(), name='subject-mechanical-engineering'),
    path('subject/meteorology',SubjectMeteorologyView.as_view(), name='subject-meteorology'),
    path('subject/mobile-development',SubjectMobileDevelopmentView.as_view(), name='subject-mobile-development'),
    path('subject/music',SubjectMusicView.as_view(), name='subject-music'),
    path('subject/nanotechnology',SubjectNanotechnologyView.as_view(), name='subject-nanotechnology'),
    path('subject/network-security',SubjectNetworkSecurityView.as_view(), name='subject-network-security'),
    path('subject/nonprofit',SubjectNonprofitView.as_view(), name='subject-nonprofit'),
    path('subject/number-theory',SubjectNumberTheoryView.as_view(), name='subject-number-theory'),
    path('subject/nursing',SubjectNursingView.as_view(), name='subject-nursing'),
    path('subject/nutrition-and-wellness',SubjectNutritionAndWellnessView.as_view(), name='subject-nutrition-and-wellness'),
    path('subject/online-education',SubjectOnlineEducationView.as_view(), name='subject-online-education'),
    path('subject/operating-systems',SubjectOperatingSystemsView.as_view(), name='subject-operating-systems'),
    path('subject/operations-management',SubjectOperationsManagementView.as_view(), name='subject-operations-management'),
    path('subject/osint',SubjectOsintView.as_view(), name='subject-osint'),
    path('subject/pedagogy',SubjectPedagogyView.as_view(), name='subject-pedagogy'),
    path('subject/pentesting',SubjectPentestingView.as_view(), name='subject-pentesting'),
    path('subject/personal-development',SubjectPersonalDevelopmentView.as_view(), name='subject-personal-development'),
    path('subject/philosophy',SubjectPhilosophyView.as_view(), name='subject-philosophy'),
    path('subject/physics',SubjectPhysicsView.as_view(), name='subject-physics'),
    path('subject/political-science',SubjectPoliticalScienceView.as_view(), name='subject-political-science'),
    path('subject/precalculus',SubjectPrecalculusView.as_view(), name='subject-precalculus'),
    path('subject/presentation-skills',SubjectPresentationSkillsView.as_view(), name='subject-presentation-skills'),
    path('subject/programming-and-software-development',SubjectProgrammingAndSoftwareDevelopmentView.as_view(), name='subject-programming-and-software-development'),
    path('subject/programming-languages',SubjectProgrammingLanguagesView.as_view(), name='subject-programming-languages'),
    path('subject/project-management',SubjectProjectManagementView.as_view(), name='subject-project-management'),
    path('subject/psychology',SubjectPsychologyView.as_view(), name='subject-psychology'),
    path('subject/public-health',SubjectPublicHealthView.as_view(), name='subject-public-health'),
    path('subject/quantum-computing',SubjectQuantumComputingView.as_view(), name='subject-quantum-computing'),
    path('subject/reading',SubjectReadingView.as_view(), name='subject-reading'),
    path('subject/red-team',SubjectRedTeamView.as_view(), name='subject-red-team'),
    path('subject/religion',SubjectReligionView.as_view(), name='subject-religion'),
    path('subject/resilience',SubjectResilienceView.as_view(), name='subject-resilience'),
    path('subject/reverse-engineering',SubjectReverseEngineeringView.as_view(), name='subject-reverse-engineering'),
    path('subject/risk-management',SubjectRiskManagementView.as_view(), name='subject-risk-management'),
    path('subject/robotics',SubjectRoboticsView.as_view(), name='subject-robotics'),
    path('subject/sales',SubjectSalesView.as_view(), name='subject-sales'),
    path('subject/science',SubjectScienceView.as_view(), name='subject-science'),
    path('subject/self-improvement',SubjectSelfImprovementView.as_view(), name='subject-self-improvement'),
    path('subject/social-sciences',SubjectSocialSciencesView.as_view(), name='subject-social-sciences'),
    path('subject/social-work',SubjectSocialWorkView.as_view(), name='subject-social-work'),
    path('subject/sociology',SubjectSociologyView.as_view(), name='subject-sociology'),
    path('subject/software-development',SubjectSoftwareDevelopmentView.as_view(), name='subject-software-development'),
    path('subject/sports',SubjectSportsView.as_view(), name='subject-sports'),
    path('subject/statistics',SubjectStatisticsView.as_view(), name='subject-statistics'),
    path('subject/stem',SubjectStemView.as_view(), name='subject-stem'),
    path('subject/strategic-management',SubjectStrategicManagementView.as_view(), name='subject-strategic-management'),
    path('subject/sustainability',SubjectSustainabilityView.as_view(), name='subject-sustainability'),
    path('subject/teacher-development',SubjectTeacherDevelopmentView.as_view(), name='subject-teacher-development'),
    path('subject/test-prep',SubjectTestPrepView.as_view(), name='subject-test-prep'),
    path('subject/textiles',SubjectTextilesView.as_view(), name='subject-textiles'),
    path('subject/threat-intelligence',SubjectThreatIntelligenceView.as_view(), name='subject-threat-intelligence'),
    path('subject/trigonometry',SubjectTrigonometryView.as_view(), name='subject-trigonometry'),
    path('subject/urban-planning',SubjectUrbanPlanningView.as_view(), name='subject-urban-planning'),
    path('subject/veterinary-science',SubjectVeterinaryScienceView.as_view(), name='subject-veterinary-science'),
    path('subject/visual-arts',SubjectVisualArtsView.as_view(), name='subject-visual-arts'),
    path('subject/web-development',SubjectWebDevelopmentView.as_view(), name='subject-web-development'),
    path('subjects',SubjectsView.as_view(), name='subjects'),
    path('universities',UniversitiesView.as_view(), name='universities'),
    path('university/columbia',UniversityColumbiaView.as_view(), name='university-columbia'),
    path('university/cornell',UniversityCornellView.as_view(), name='university-cornell'),
    path('university/duke',UniversityDukeView.as_view(), name='university-duke'),
    path('university/edinburgh',UniversityEdinburghView.as_view(), name='university-edinburgh'),
    path('university/gatech',UniversityGatechView.as_view(), name='university-gatech'),
    path('university/harvard',UniversityHarvardView.as_view(), name='university-harvard'),
    path('university/iit-kharagpur',UniversityIitKharagpurView.as_view(), name='university-iit-kharagpur'),
    path('university/iitm',UniversityIitmView.as_view(), name='university-iitm'),
    path('university/mit',UniversityMitView.as_view(), name='university-mit'),
    path('university/penn',UniversityPennView.as_view(), name='university-penn'),
    path('university/purdue',UniversityPurdueView.as_view(), name='university-purdue'),
    path('university/rice',UniversityRiceView.as_view(), name='university-rice'),
    path('university/stanford',UniversityStanfordView.as_view(), name='university-stanford'),
    path('university/umich',UniversityUmichView.as_view(), name='university-umich'),
    path('collection/ivy-league-moocs',CollectionIvyLeagueMoocsView.as_view(), name='collection-ivy-league-moocs'),
    path('collection/ivy-league-moocs/',CollectionIvyLeagueMoocsView.as_view(), name='collection-ivy-league-moocs-'),
    path('report/',ReportView.as_view(), name='report-'),
    path('report/100-most-popular-online-courses-2021/',Report100MostPopularOnlineCourses2021View.as_view(), name='report-100-most-popular-online-courses-2021-'),
    path('report/2022-year-in-review/',Report2022YearInReviewView.as_view(), name='report-2022-year-in-review-'),
    path('report/author/dhawal/',ReportAuthorDhawalView.as_view(), name='report-author-dhawal-'),
    path('report/author/heba/',ReportAuthorHebaView.as_view(), name='report-author-heba-'),
    path('report/author/manoel/',ReportAuthorManoelView.as_view(), name='report-author-manoel-'),
    path('report/author/ruima/',ReportAuthorRuimaView.as_view(), name='report-author-ruima-'),
    path('report/best-bookkeeping-courses/',ReportBestBookkeepingCoursesView.as_view(), name='report-best-bookkeeping-courses-'),
    path('report/best-css-layout-courses/',ReportBestCssLayoutCoursesView.as_view(), name='report-best-css-layout-courses-'),
    path('report/best-digital-art-courses/',ReportBestDigitalArtCoursesView.as_view(), name='report-best-digital-art-courses-'),
    path('report/best-elm-courses/',ReportBestElmCoursesView.as_view(), name='report-best-elm-courses-'),
    path('report/best-free-online-courses-2021/',ReportBestFreeOnlineCourses2021View.as_view(), name='report-best-free-online-courses-2021-'),
    path('report/best-free-online-courses-2022/',ReportBestFreeOnlineCourses2022View.as_view(), name='report-best-free-online-courses-2022-'),
    path('report/best-resume-writing-courses/',ReportBestResumeWritingCoursesView.as_view(), name='report-best-resume-writing-courses-'),
    path('report/chinese-mooc-platforms/',ReportChineseMoocPlatformsView.as_view(), name='report-chinese-mooc-platforms-'),
    path('report/class-central-ddos-attack/',ReportClassCentralDdosAttackView.as_view(), name='report-class-central-ddos-attack-'),
    path('report/coursera-free-online-courses/',ReportCourseraFreeOnlineCoursesView.as_view(), name='report-coursera-free-online-courses-'),
    path('report/coursera-google-new-deal/',ReportCourseraGoogleNewDealView.as_view(), name='report-coursera-google-new-deal-'),
    path('report/coursera-top-courses/',ReportCourseraTopCoursesView.as_view(), name='report-coursera-top-courses-'),
    path('report/cs50-free-certificate/',ReportCs50FreeCertificateView.as_view(), name='report-cs50-free-certificate-'),
    path('report/edx-top-courses/',ReportEdxTopCoursesView.as_view(), name='report-edx-top-courses-'),
    path('report/emoocs-2023-cfp/',ReportEmoocs2023CfpView.as_view(), name='report-emoocs-2023-cfp-'),
    path('report/feed/',ReportFeedView.as_view(), name='report-feed-'),
    path('report/free-certificates/',ReportFreeCertificatesView.as_view(), name='report-free-certificates-'),
    path('report/free-google-certifications/',ReportFreeGoogleCertificationsView.as_view(), name='report-free-google-certifications-'),
    path('report/futurelearn-price-hike-ceo-exit/',ReportFuturelearnPriceHikeCeoExitView.as_view(), name='report-futurelearn-price-hike-ceo-exit-'),
    path('report/google-free-certificates/',ReportGoogleFreeCertificatesView.as_view(), name='report-google-free-certificates-'),
    path('report/harvard-cs50-guide/',ReportHarvardCs50GuideView.as_view(), name='report-harvard-cs50-guide-'),
    path('report/india-online-degrees/',ReportIndiaOnlineDegreesView.as_view(), name='report-india-online-degrees-'),
    path('report/linkedin-learning-free-learning-paths/',ReportLinkedinLearningFreeLearningPathsView.as_view(), name='report-linkedin-learning-free-learning-paths-'),
    path('report/list-of-mooc-based-microcredentials/',ReportListOfMoocBasedMicrocredentialsView.as_view(), name='report-list-of-mooc-based-microcredentials-'),
    path('report/masterclass-layoffs-round-three/',ReportMasterclassLayoffsRoundThreeView.as_view(), name='report-masterclass-layoffs-round-three-'),
    path('report/mooc-based-masters-degree/',ReportMoocBasedMastersDegreeView.as_view(), name='report-mooc-based-masters-degree-'),
    path('report/most-cited-mooc-research/',ReportMostCitedMoocResearchView.as_view(), name='report-most-cited-mooc-research-'),
    path('report/most-popular-courses-2022/',ReportMostPopularCourses2022View.as_view(), name='report-most-popular-courses-2022-'),
    path('report/most-popular-courses-2023/ ',ReportMostPopularCourses2023View.as_view(), name='report-most-popular-courses-2023- '),
    path('report/most-popular-online-courses/',ReportMostPopularOnlineCoursesView.as_view(), name='report-most-popular-online-courses-'),
    path('report/open-university-insiders-perspective/',ReportOpenUniversityInsidersPerspectiveView.as_view(), name='report-open-university-insiders-perspective-'),
    path('report/udemy-layoffs/',ReportUdemyLayoffsView.as_view(), name='report-udemy-layoffs-'),
    path('report/udemy-top-courses/',ReportUdemyTopCoursesView.as_view(), name='report-udemy-top-courses-'),
    path('report/online-learning-deals/',ReportOnlineLearningDeals.as_view(), name='report-online-learning-deals'),
    path('report/category/best-courses/',ReportCategoryBestCourses.as_view(), name='report-category-best-courses'),



]

