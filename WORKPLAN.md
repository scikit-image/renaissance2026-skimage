## Short Summary

*Edit as needed from LOI. Briefly describe the purpose of the proposal and the software project(s) it involves. Please note that details related to the work plan can be moved to and expanded upon in the Work Plan and Goals, Outcomes, Milestones and Deliverables section.*

*3,000 characters maximum*

scikit-image is a foundational open-source image-processing library in the scientific Python ecosystem. Since 2009 it has provided a curated, well-documented, and tested collection of algorithms for filtering, segmentation, morphology, measurement, and more. Life scientists rely on it to turn microscopy, neuroimaging, and cell data into quantitative results. It is downloaded ~30M times monthly, has over 8000 citations, and underpins many bioimaging pipelines.

With instruments of increasing sophistication, such as light-sheet fluorescence microscopes, and the production of high-volume data products enabled by AI and foundation models, life-science imaging is outgrowing its open-source foundation. Datasets now routinely grow to terabytes and analysis increasingly relies on a combination of deep learning and classic algorithms, deployed via agentic pipelines. Yet, the implementations of those classical image-processing routines, including the ones in scikit-image, were built in a time when they were typically deployed, by hand, on a single machine: CPU-bound, albeit with several cores. Scientists who depend on our vetted, thoroughly tested algorithms cannot currently easily scale to modern data and hardware, and agentic pipeline generation can be less efficient than it needs to be. The researchers must then turn to niche tools outside of the ecosystem to access capabilities such as registration. Our goal is for our users to keep using trusted, community-built software as their work scales and moves to modern hardware. For scikit-image, the timing for this change is ideal, with version 2.0, a major API overhaul, slated for completion in fall 2026.

We propose a coordinated 24-month project, organized around five mutually reinforcing goals. Four of these are concrete technical objectives: (1) hardware acceleration, enabling GPU workflows so that large image volumes can be processed at far higher rates; (2) AI-accessible documentation, porting our docs to mystmd, whose machine-readable output lets coding agents efficiently discover and correctly compose our functions; (3) image registration, hardening existing experimental APIs into a single, robust module usable across bioimaging disciplines; and (4) procedures for AI-assisted maintenance, discovering and openly sharing reusable patterns for safely applying AI to routine upkeep, freeing developer time for algorithmic work. The fifth goal, community engagement, supports and may help refine the above goals: via annual community and developer summits we validate and refine our technical priorities through feedback from bioimaging researchers and neighboring projects (NiPy, DiPy, napari, DeepLabCut), ensuring the work addresses real research needs.

# Work Plan

Open Source for the Life Sciences (OS4LS)

**Proposal Title:** Accelerating scikit-image for modern bioimaging workflows

**Applicant Name:** Stéfan van der Walt

---

## Work Plan (max 750 words)

scikit-image provides a curated set of carefully tested & documented, community-owned image processing algorithms widely deployed in life sciences research. This proposal supports a 24-month effort to evolve the trusted foundation scikit-image provides to meet modern demands: processing large datasets, utilizing GPU hardware, and implementing pipelines with the assistance of AI. This work fits the project roadmap ([SKIP 4](https://scikit-image.org/docs/dev/skips/4-transition-to-v2.html)), which aims to complete the library's major 2.0 API overhaul by fall 2026. The new API, apart from being more uniform and addressing concerns around early design decisions, generalizes the library for use across more imaging modalities, and opens the door to new feature development.

We structure our work around five goals that augment one another. Four are concrete technical objectives, identified as priorities for the bioimaging community---hardware acceleration, AI-accessible documentation, image registration, and AI-assisted maintenance (Goals 1--4, detailed below). The fifth is community engagement, which allows for early feedback, and ensures that the technical work is grounded in real research needs.

**Goal 1. Hardware acceleration:** We will make scikit-image competitive on modern hardware by enabling GPU processing. In discussion with the Array API team and Cython authors, we have formulated a strategy for optimizing scikit-image across hardware platforms, and across both vectorized and non-vectorized classes of algorithms. This will make it possible to process larger images at a much higher rate.

**Goal 2. AI-accessible documentation:** We will port our documentation to mystmd, whose machine-readable output lets AI agents better discover and use scikit-image. Together with researchers in the community, we will experiment with automated pipeline construction of bioimaging workflows, improving the library and its documentation wherever necessary to improve success rates.

**Goal 3. Image registration:** As a concrete technical deliverable, we will substantially improve our image-registration support. This functionality is commonly requested by researchers across life science research fields, who currently often have to bolt together pipelines that depend on bespoke command-line utilities. We have implemented experimental APIs, suitable across a diverse set of applications such as neuroimaging, microscopy, and cell tracking, that we wish to solidify.

**Goal 4. Structured, AI-assisted maintenance:** We operate in a rapidly changing technological landscape; one in which AI offers clear benefits alongside known risks. The purpose of this goal is to uncover methods for AI-assisted maintenance, not the maintenance work itself (although that will automatically follow). Working with colleagues across the scientific Python ecosystem, we will explore and write up reusable patterns and skills for carefully integrating AI into open-source maintenance workflows (especially mechanistic tasks, such as dependency updates, deprecations, CI failures, security fixes, resolution of merge conflicts, etc.), and disseminate them openly for other projects to adopt. This goal aims to lift the routine maintenance burden from developers, so they can spend their time on algorithmic work that requires experience, in-depth field knowledge, and careful deliberation.

**Goal 5: Community engagement.** We engage the life sciences research community to ensure that scikit-image, as well as the technical goals outlined above, cover their use cases. Through annual Community Summits---connecting first with known groups, the Advanced Bioimaging Lab (Berkeley) and the Van Valen Lab (Caltech), and then expanding to others---we validate and refine the above technical goals, and surface new needs. We then convene annual Developer Summits, bringing together scikit-image developers alongside other ecosystem developers with shared concerns (NiPy, DiPy, napari, DeepLabCut), to discuss and implement solutions.

scikit-image is permissively licensed under the Modified BSD license. All work funded by this grant is available to researchers across the globe free of charge and free of restriction.

Beyond funded activities, the Berkeley Institute for Data Science will provide in-kind support for summits in the form of meeting space in their AI Futures Lab.

---

<!--
May want to say something about how projects currently handle, e.g., registration deficiencies:

, currently handled with ad hoc script, niche tools, or crude workarounds
-->

---

## Goals, Outcomes, Milestones and Deliverables (up to 5 goals, not included in the 750-word limit)

---

### Goal 1: Hardware acceleration

**Outcome:** Scientists run scikit-image on GPUs to process large datasets.

**Milestones & Deliverables:**

1.1 Finalize an implementation plan in collaboration with the Array API team and Cython developers. [Year 1]

1.2 Prototype an initial GPU implementation for several different types of algorithms. [Year 1]

1.3 Form a plan, based on the above experience, for bringing scikit-image as near as possible to 100% GPU coverage. [Year 2]

1.4 Implement GPU accelerated routines for the majority of the library, focusing on most used functionality and documenting progress & exceptions. [Year 2]

**Success indicators:**

- Benchmarks for several highly used scikit-image algorithms show significant performance improvement on GPUs.
- Documentation indicates which functions are accelerated this way.

---

### Goal 2: AI-accessible documentation

**Outcome:** Documentation is ported to mystmd. Coding agents can easily discover and correctly compose scikit-image functions.

**Milestones & Deliverables:**

2.1 Port scikit-image documentation to mystmd. [Year 1]

2.2 Build and test, in collaboration with partners, a few end-to-end reference bioimaging workflows, validated with AI agents. [Year 1-2]

2.3 Address library and documentation gaps surfaced by workflow testing. [Year 2]

**Success indicators:**

- Front page, along with user and reference documentation, is migrated to mystmd.
- Prototype workflows can be auto-generated, correctly, start-to-end.

---

### Goal 3: Image registration

**Outcome:** Researchers in neuroimaging, microscopy, and cell tracking gain access to a single, robust registration implementation in scikit-image.

**Milestones & Deliverables:**

3.1 Complete design of a general registration API covering core use cases across target domains, building on the existing prototype. [Year 1]

3.2 Implement and test core registration algorithms (e.g., rigid, affine, deformable) against reference datasets. [Year 1-2]

3.3 Validate the new registration module against real workflows with partner projects (DiPy, NiPy, Van Valen Lab) across at least two domains. [Year 2]

**Success indicators:**

- General-purpose registration module released.
- Module is adopted in at least two research pipelines of varying modalities.

---

### Goal 4: Structured, AI-assisted maintenance

**Outcome:** The community gains reusable, openly published patterns and skills for safely applying AI to open-source maintenance. For scikit-image itself, maintainers shift effort from routine upkeep toward algorithmic work, stabilizing the pace of development without a reduction in quality, and without a significant increase in code complexity that would undermine maintainability.

**Milestones & Deliverables:**

4.1 In collaboration with colleagues from the scientific Python ecosystem, explore and document patterns for safely applying AI to open-source maintenance tasks. [Year 1]

4.2 Validate and refine these patterns against scikit-image's own maintenance workflows. [Year 1-2]

4.3 Publish the resulting skills and patterns as an open, reusable resource for the broader community. [Year 1-2]

**Success indicators:**

- A published, documented set of AI-maintenance patterns/skills, adopted by at least one other ecosystem project.
- For scikit-image, a measurable shift of maintainer time toward algorithmic/feature work, with reduced time-to-resolution on routine issues/PRs.

---

### Goal 5: Community engagement

**Outcome:** Bioimaging researchers gain access to scikit-image routines that address existing workflow shortcomings.

**Milestones & Deliverables:**

5.1 Host community summit to conduct needs assessment with the Advanced Bioimaging Lab (Berkeley) and the Van Valen Lab (Caltech); publish a prioritized roadmap of candidate routines. [Year 1]

5.2 Host developer summit for scikit-image developers. [Year 1]

5.3 Implement and release solutions to highest priority needs identified in 5.1. [Year 1]

5.4 Host community summit to assess needs across wider life sciences community, and to report back on previous progress. [Year 2]

5.5 Host developer summit that extends to more image processing developers in the community, such as NiPy, DiPy, napari, and DeepLabCut. [Year 2]

5.6 Implement and release solutions to highest priority needs identified in 5.4. [Year 2]

**Success indicators:**

- Meetings are held, engaging at least 20–30 people.
- At least 5 major features are added to the library in response to community needs.

<!--
DEFERRED FOR NEXT EDITING ROUND (from review, 2026-07-20):
- Use the word-count headroom in the 750-word narrative (currently ~560 words).
- Add quantitative success indicators:
    * Goal 1 (Hardware): target speedup (e.g. >=10x) and rough count/list of
      high-use functions expected GPU-covered by end of Year 2.
    * Goal 2 (Docs): quantify agent-reproducible reference workflows
      (N workflows, not just "correctly, start-to-end").
- Expand in-kind contributions beyond BIDS meeting space: PI/maintainer time,
  existing CI credits and test infrastructure.

RESOLVED:
- Roadmap link: added SKIP 4 in the narrative.
- Pythran: not added to the Hardware goal. Pythran is a CPU/SIMD transpiler and
  does not facilitate GPU acceleration, so the LOI's Pythran mention does not
  need mirroring here; the GPU story stays with the Array API team and Cython.
-->

