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

scikit-image is the foundational image-processing library of the scientific Python ecosystem. Since 2009 it has provided a curated, well-documented, permissively licensed collection of algorithms—filtering, segmentation, feature detection, morphology, measurement, and registration—that life scientists rely on to turn microscopy, medical, and other imaging data into quantitative results. The 2014 PeerJ paper has been cited more than 8,000 times, the library is downloaded roughly 28 million times per month (about 6.6 million in the last week alone), and it sits beneath much of the modern bioimaging stack, including cellpose and countless lab-specific analysis pipelines.

For several years the core team has concentrated on a major internal effort: the scikit-image 2.0 API. This work modernizes our interface, brings every function in line with current best practices, and implements consistent design protocols across the library. It is healthy, necessary work—but it has kept us focused on refactoring and software-engineering mechanics rather than on new capabilities for our users. With this grant, we will turn our attention back to the scientists who depend on us, and to the life-science imaging community in particular.

We propose five lines of work:

1. **Community engagement and enabling pathways.** We will systematically learn the needs of the bioimaging community and build the routines those projects can stand on—working with the NiPy and DiPy teams, the napari developers, packages such as DeepLabCut, the Van Valen lab (Caltech), and the Advanced Bioimaging Center at Berkeley. We will implement these capabilities in scikit-image, in collaboration with those teams, rather than writing code directly into their libraries.

2. **Hardware acceleration.** We will make scikit-image competitive on modern hardware by enabling GPU workflows. The Array API standard helps, but is insufficient for a predominantly Cython-based library; we will coordinate with the Cython team and explore complementary technical pathways.

3. **AI-accessible documentation.** We will port our documentation to MyST Markdown, whose machine-readable JSON output lets agents and AI tools discover and use scikit-image far more reliably. We will build and test end-to-end bioimaging workflows, improving the library and its docs wherever those workflows break down.

4. **Image registration.** As a concrete technical deliverable, we will substantially expand our image-registration support—today only a basic API—into a robust, general offering valuable across neuroimaging, microscopy, and many other life-science domains.

5. **Structured, AI-assisted maintenance.** We will integrate AI into our maintenance workflows deliberately—handling dependency updates, deprecations, CI failures, and security fixes—to reduce our backlog and free developer time for algorithmic work.

Together, these aims align with scikit-image's own roadmap and carry the backing of the core maintainer team.

---

## Expected Value

If the proposal is successfully funded, what does success look like? We're seeking to understand:
- what type of capabilities the proposal is unlocking for the scientific community;
- how upstream and downstream software will be improved by the proposal;
- how the proposed work supports or implements novel functionality for AI enablement and large-scale data analysis.

*1,500 characters maximum*

Success means scikit-image becomes a first-class tool for AI-native, large-scale bioimaging—not only a manual, single-machine library.

For the scientific community, this unlocks GPU-accelerated processing of the large image volumes now routine in microscopy and medical imaging; reliable use of scikit-image inside agentic and AI-assisted workflows, through machine-readable documentation and tested end-to-end pipelines; and a substantially expanded image-registration capability that many life-science fields currently assemble by hand or borrow from heavier, domain-specific tools.

Upstream, our GPU work will exercise and improve the Array API standard and Cython for the whole ecosystem. Downstream, the tools that use scikit-image—from cellpose to custom lab pipelines—gain faster execution and clearer interfaces; and partner projects such as NiPy, DiPy, DeepLabCut, and napari gain new registration and bioimaging routines they can build on, developed in collaboration rather than committed into their codebases.

On AI enablement specifically: machine-readable docs let coding agents call our functions correctly; tested reference workflows give AI systems reliable building blocks; and GPU support brings scikit-image into the data-intensive training and inference loops that modern bioimaging increasingly depends on.

---

## Landscape Analysis

We are looking for proposals from software projects with demonstrated traction and adoption. Briefly describe other software tools that the audience for this proposal primarily uses (including proprietary alternatives, if they exist), and how the software project(s) in your proposal compare in terms of user base, adoption, functionality, and maturity relative to their target audience. You can add indicators of adoption and usage as needed. Please indicate if the software is used in AI applications and workflows.

*1,500 characters maximum*

Bioimage analysts work across a spectrum of tools. ImageJ/Fiji and CellProfiler dominate GUI-driven analysis; ITK is the standard for medical registration and segmentation; OpenCV serves computer vision; and commercial packages (Imaris, MATLAB, Arivis) remain common in microscopy. napari has become the leading Python-based viewer. Among these, scikit-image is the general-purpose, Pythonic image-processing foundation: BSD-licensed, thoroughly documented, and designed to interoperate with NumPy, SciPy, and the wider scientific Python stack.

Its adoption is exceptional: more than 8,000 citations of the 2014 PeerJ paper, roughly 28 million downloads per month, and a core dependency role beneath cellpose and a large fraction of custom bioimaging pipelines. It is already the de-facto image-processing layer that deep-learning workflows reach for when preparing, augmenting, and measuring image data—its metrics such as structural similarity (SSIM) are standard loss and evaluation functions for training and benchmarking image models, including microscopy denoising and super-resolution.

Relative to its peers, scikit-image is more mature and more broadly adopted than most open alternatives, fully open unlike the commercial tools, and uniquely positioned as the composable, scriptable layer that AI-driven pipelines require. Its current gaps—GPU performance and AI-discoverable interfaces—are addressed by this proposal.

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

I am the founder of scikit-image and a member of its core maintainer team. I
confirm that the work proposed here is aligned with the scikit-image roadmap and
has the support of the core maintainer community. As co-founder of Scientific
Python and a core contributor across NumPy, SciPy, NetworkX, and (previously)
DiPy, I will coordinate the proposed work and the collaborations with partner
groups in the bioimaging community.
