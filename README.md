The purpose of this project is for you to achieve all learning outcomes of the course. The process of working through it is more valuable than the mark received.
In attempting and completing this project correctly, you will:
  • experience sourcing real, raw data
  • refine your data wrangling skills
  • encounter real data problems and employ the tools and techniques learned in this class and beyond to solve them
  • improve your data-based problem-solving skills
  • be patient when completing your work

This wrangling project is an exploration of public data with an intention to discover insights of interest to New Zealand or a global audience. The project is split into two parts: project proposal and project report.You should follow the steps described in the following sections in the order that they are listed.

Project should be sufficiently interesting (i.e. worth doing), doable, and be of similar complexity to other projects (to ensure fairness in marking and learning experience). To ensure your project meets this standard, please spend sufficient time to read the project requirements, explore potential datasets, and plan your project.

Summarise your plan in a project proposal document which briefly states:
1. The two datasets you will use in the project
  o At least one dataset must be from the list provided here. Use these datasets to form the basis for your project. We ask you to use at least one provided dataset to
  simulate a real working environment, where you may be tasked with analysing data on a particular initial topic and must then find additional resources to support your
  findings
  o Clearly state the sources: what are the data, their file types and where do they come from?
  o Provide links to the source of the files
2. How you plan to combine the two datasets
  o Consider what attribute(s) they have in common
  o Consider what technique(s) you plan to use
3. The intended final format of your combined dataset (e.g. Excel workbook, SQL database, MongoDB store, etc.)
4. A backup plan for completing this project
  o Consider what you could do to avoid forfeiting all 15% of your final grade due to poor forethought or underestimation of the requirements of this project etc.
  o You should enact this plan if you are unable to successfully combine your two datasets by Week 11
  
  
Source and audit two disparate datasets from separate sources. You will be required to combine the datasets into a single dataset, so ensure the chosen datasets are suitably related.

your datasets must be:
• sufficiently different in format/file type from one another, and
• sufficiently complex - complexity can arise from
o large data size (e.g. tens of thousands of rows/instances, or tens of columns) 
o non-uniform data structures (e.g. the data is an amalgamation from multiple sources, or different attributes exist for different instances)
o dirty data

Summarise your sourcing and auditing activities in the report

Pose three meaningful questions that could only be answered if the two datasets were combined. These questions should be impossible to answer if the datasets were not combined. You can assume any problem or situation/scenario under which these questions are posed. You will be required to attempt to answer the questions in your report, whether you obtain correct answers is not important as long as your attempt is sensible

Wrangle your two datasets to clean and combine them into a single dataset. Store the combined dataset in a single data store (i.e. its “final storage format”). Data stores could be a file (e.g. Excel workbook) or a database (e.g. Microsoft SQL Server, Microsoft Access, SQLite, MongoDB). You must not use any file converter or automation tool to transform data.

If your datasets are too large for the tools used in this course to handle, you may use a sufficiently large subset of the data to build a proof-of-concept that the data can in fact be combined.

Using your cleaned and combined dataset in its “final storage format”, attempt to answer the three questions you posed in any way you can. Answering is likely to involve the use of one or many of the following: PivotTables, XPath, MongoDB queries, visualisations, SQL queries etc.

You are advised to keep your exploration simple. Bear in mind that the learning outcomes of this assessment relate to data wrangling process and technique but not statistical analysis or data mining.


Document the previous tasks in one report. Lay out your report in three sections in this order:
1) Project Summary
2) Wrangling Details
3) Questions and Answers
The requirements of each section are as the following.

3.6.1 Project Summary
Write this section for a business audience (e.g. a senior business decision maker).
Summarise your entire project. Include the three questions you posed, each with a short summary and discussion of your answer/conclusion for it. Provide some insight about your findings.

3.6.2 Wrangling Details
Write this section for a “data expert” audience (e.g. a classmate).
Detail the following wrangling processes in your report. Specifically:
For each dataset
  • Its origin. Provide a direct link to the data, or if that is not possible, explain how you obtained the data
  • Its general characteristics. What format is it in; what is the structure; how many columns/fields; how many records? etc.
  • An initial audit. What observations did you make about the data? Are there any obvious or potential problems that may have to be dealt with before combining it
    with the other dataset? Steps you performed to combine the datasets
  • The level of detail should be so that any of your classmates can replicate the process
  o Stating what you did is more important than stating how you did it. For example, rather than explaining what menu items you clicked on, it is sufficient to state       that you “removed duplicates on the user id and timestamp fields”
  o Include relevant screenshots of intermediate steps etc.
  • State all transformations performed on each dataset individually before they were combined
  • State all transformations performed to combine the datasets
  • State the steps performed to store the combined dataset in its “final storage format”
  
  
3.6.3 Questions and Answers
Write this section for a “data expert” audience (e.g. a classmate).
Detail how you used your combined dataset, in its “final storage format”, to reach the answers/conclusions to your questions. Specifically:
For each question
  • State the question and your answer/conclusion
  • State the steps performed to produce the answer. Include what tools/software you used and what queries you executed etc.
  o The goal here is not so that the process can be replicated, but to show your answer/conclusion is sound or otherwise reasonable
  o Even if no exact answer was found, the steps to reach that result still need to be documented. You should also state what would be needed to reach an answer
  o Include relevant screenshots of intermediate steps etc.

