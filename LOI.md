# Proposal

---

# Section 1: Applicant Information

## First Name

Stéfan

---

## Last Name

van der Walt

---

## Email

This email address will be used for all communications and notifications about this proposal.

stefanv@berkeley.edu

---

## Organizational or Institutional Affiliation

The applicant's main organizational or institutional affiliation. Note that this may be different from the organization receiving the grant.

Berkeley Institute for Data Science (BIDS), University of California, Berkeley

---

## Country of Residence

*(dropdown — full country list)*

United States

---

## Have you ever received funding as a grantee under the CZI EOSS program?

If you were previously funded by the Chan Zuckerberg Initiative as a PI/grant lead, please select Yes. This field does not impact the evaluation of your proposal.

- (X) Yes
- ( ) No

---

## Organization Name

If the proposal is considered for funding, this will be the organization receiving the grant. Note that this may be different from the main affiliation of the applicant. You will be able to provide additional information during the Full Proposal stage, if invited to apply.

NumFOCUS, Inc.

---

## Organization Website

*(URL)*

https://numfocus.org

---

## Organization Country

*(dropdown — full country list)*

United States

---

## Organization Type

- ( ) Academic Institution
- (X) Fiscal sponsor
- ( ) Other Non-profit
- ( ) Industry/company
- ( ) Government

---

# Section 2: Proposal Information

---

## Proposal Title

*60 characters maximum*

Accelerating scikit-image for modern bioimaging workflows

<!-- 44 characters. Alternatives:
     - "Modernizing scikit-image for the life sciences" (47)
     - "scikit-image: bioimaging for the AI era" (39)
-->

---

## Short Summary

Briefly describe the purpose of the proposal and the software project(s) it involves.

*3,000 characters maximum*

scikit-image is a foundational open-source image-processing library in the scientific Python ecosystem. Since 2009 it has provided a curated, well-documented and tested collection of algorithms: for filtering, segmentation, feature detection, morphology, measurement, and registration. Life scientists rely on scikit-image to analyze microscopy, neuroimaging, and cell data into quantitative research results. The library is downloaded roughly 30M times per month, and its 2014 paper has been cited more than 8000 times. Is is a fundamental building block for modern bioimaging stacks, and is used in a great variety of lab analysis pipelines.

For the last few years, the core team has been working on a major internal refactor: the scikit-image 2.0 API. This work modernizes our interface, brings functions in line with current best practices, and establishes consistent design protocols across the library. This was necessary and important work, but it has also kept us focused on refactoring and software-engineering mechanics, rather than on bringing new capabilities to the community. With this grant, we aim to turn our attention back to the scientists who depend on us, and to the life-science imaging community in particular.

We propose five lines of work:

1. **Community engagement and enabling pathways.** We will systematically learn the current needs of the bioimaging community and, in response, build new routines for scikit-image to address those. Initially, we will rely on our established connections with  the Advanced Bioimaging Lab at Berkeley and the Van Valen lab at Caltech, but will expand to include input from other groups as the grant progresses. On the software side, we will closely collaborate with the NiPy, DiPy, and napari developers, later expanding to domain-specific projects such as DeepLabCut.

2. **Hardware acceleration.** We will make scikit-image competitive on modern hardware by enabling GPU workflows. The Array API standard helps, is insufficient by itself for a predominantly Cython-based library; we will coordinate with the Cython team and Pythran author to explore complementary technical pathways.

3. **AI-accessible documentation.** We will port our documentation to MyST Markdown, whose machine-readable JSON output lets agents and AI tools better discover and use scikit-image. We will build and test end-to-end bioimaging workflows, improving the library and its docs wherever those workflows are incomplete or of insufficient quality.

4. **Image registration.** As a concrete technical deliverable, we will substantially expand our image-registration support. We have an existing, basic API, but we want to see it become a robust, general offering practically usable across neuroimaging, microscopy, cell tracking, and other fields.

5. **Structured, AI-assisted maintenance.** We will, carefully, explore and integrate AI into our maintenance workflows, particularly lifting the burden on routine maintenance tasks (dependency updates, deprecations, CI failures, security fixes, etc.) that occupy a lot of the team's time. This should help us reduce our backlog and free developer time for algorithmic work, which still requires deep expertise and focus.

These five aims align with scikit-image's own roadmap and carry the backing of the core maintainer team.

---

## Expected Value

If the proposal is successfully funded, what does success look like? We're seeking to understand:
- what type of capabilities the proposal is unlocking for the scientific community;
- how upstream and downstream software will be improved by the proposal;
- how the proposed work supports or implements novel functionality for AI enablement and large-scale data analysis.

*1,500 characters maximum*

Success means that scikit-image remains a relevant, highly-used library for large-scale bioimaging, providing cutting edge algorithmic access across thousands of projects.

For the scientific community, we unlock GPU-accelerated processing of the large image volumes now routine in microscopy and medical imaging; reliable use of scikit-image inside agentic and AI-assisted workflows, through machine-readable documentation and tested end-to-end pipelines; and a substantially expanded image-registration capability that many projects currently assemble by hand or borrow from heavier, domain-specific tools.

Upstream, our GPU work will exercise and improve dispatching and Array API standards, potentially improving compilers like Cython and Pythran for the whole ecosystem. Downstream, projects that use scikit-image gain faster execution and cleaner interfaces, while partner projects such as NiPy and DiPy gain new registration and bioimaging building blocks, developed by an experienced, trusted team.

In an era where AI is becoming ever more relevant: machine-readable docs let coding agents call our functions correctly; tested reference workflows give AI systems reliable building blocks; and GPU support makes scikit-image effective in data-intensive workflows and the training/inference loops that modern bioimaging increasingly depends on.

---

## Landscape Analysis

We are looking for proposals from software projects with demonstrated traction and adoption. Briefly describe other software tools that the audience for this proposal primarily uses (including proprietary alternatives, if they exist), and how the software project(s) in your proposal compare in terms of user base, adoption, functionality, and maturity relative to their target audience. You can add indicators of adoption and usage as needed. Please indicate if the software is used in AI applications and workflows.

*1,500 characters maximum*

Bioimage analysts use a wide spectrum of tools. ImageJ/Fiji and CellProfiler are common for GUI-driven analysis; ITK is the standard for medical registration and segmentation; OpenCV serves robotics and computer vision; and commercial packages (Imaris, MATLAB, Arivis) remain common in microscopy. napari has become the leading Python-based viewer. Next to these, scikit-image is the reference Pythonic image-processing implementation: it has a clean API, wide algorithmic support, is thoroughly tested and documented, and is designed to interoperate seamlessly with NumPy, SciPy, and the wider scientific Python ecosystem.

It is downloaded ~30M times per month, has more than 8000 citations of its 2014 paper, and is a core dependency of most Python bioimaging pipelines. Its components are widely used in scaffolding deep-learning workflows: for preparing, augmenting, and measuring results. And metrics such as structural similarity (SSIM) are widely used in training, for purposes such as microscopy denoising and super-resolution enhancement.

scikit-image is mature and broadly adopted. Its liberal license, along with transparent development and governance, make it a safe long-term infrastructure choice. Its open, well-documented API positions it uniquely  to be a composable, scriptable layer acessible to AI-driven pipelines. This proposal addresses current gaps: GPU performance, even better AI-discoverability, and an expanded algorithmic offering for bioimaging.

---

## Software Projects to be Supported

In this section you can list up to five open source software projects that will participate in this proposal. You can add projects using the "+Create" button, and include links to their repositories.

*(subform — up to 5 entries)*

1. **scikit-image** — https://github.com/scikit-image/scikit-image
   (Documentation and project site: https://scikit-image.org)

---

## Categories

Please check up to three tags describing the type of software and its target scientific audience.

**Software type:**
- [ ] Data formats and storage
- [ ] Knowledge representation and ontologies
- [X] Scientific computing
- [ ] Statistical modeling
- [ ] Workflows and computational pipelines
- [ ] Data visualization
- [ ] Interoperability
- [ ] Software ecosystem infrastructure
- [X] Hardware acceleration and scalability
- [ ] Machine learning frameworks
- [ ] Agentic frameworks
- [ ] Benchmarking and evaluation tools

**Scientific domain:**
- [ ] Genomics and transcriptomics
- [ ] Structural and molecular biology
- [ ] Cell and developmental biology
- [ ] Evolutionary biology
- [ ] Immunology
- [X] Biological and biomedical imaging
- [ ] Bioinformatics and computational biology
- [ ] Synthetic biology
- [ ] Spatial biology
- [ ] Neuroscience
- [ ] Infectious disease and epidemiology
- [ ] Computational drug discovery
- [ ] Other

<!-- Up to three tags total are allowed. Selected: Scientific computing,
     Hardware acceleration and scalability, Biological and biomedical imaging.
     Candidate swaps if you prefer a different emphasis: Interoperability or
     Agentic frameworks (software type); Neuroscience (domain). -->

---

## Funding Track

For full instructions about the track for this call, visit the provided link.

- ( ) Track 1: Domain-specific Tools
- (X) Track 2: Foundational Libraries and Ecosystem Initiatives

---

# Section 3: PI Involvement & Policies

<!-- Not in the original template scaffold, but the call lists a "Statement of
     PI involvement" as a required LOI element, plus acceptance of program
     policies. Draft statement below for the likely free-text / checkbox field. -->

## Statement of PI Involvement

I am the founder of scikit-image and a member of its core maintainer team. I confirm that the work proposed here is aligned with the scikit-image roadmap and has the support of the core maintainer community. As co-founder of Scientific Python and a core contributor across NumPy, SciPy, NetworkX, and (previously) DiPy, I commit to coordinating the proposed work and the collaborations with partner groups in the bioimaging community.
