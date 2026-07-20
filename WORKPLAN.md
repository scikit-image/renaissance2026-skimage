# Work Plan

Open Source for the Life Sciences (OS4LS)

**Proposal Title:** Accelerating scikit-image for modern bioimaging workflows

**Applicant Name:** Stéfan van der Walt

---

## Work Plan (max 750 words)

scikit-image provides a curated set of carefully tested & documented, community-owned image processing algorithms widely deployed in life sciences research. This proposal supports a 24-month effort to evolve the trusted foundation scikit-image provides to meet modern demands: processing large datasets, utilizing GPU hardware, and implementing pipelines with the assistance of AI. The project fits with the project roadmap, which aims to complete the library's major 2.0 API overhaul by fall 2026. The new API, apart from being more uniform and addressing concerns around early design decisions, generalizes the library for use across more imaging modalities, and opens the door to new feature development.

We structure our work around five goals that augment one another.

**Goal 1**, which reflects our primary mission, is to **engage the life sciences research community** to ensure that scikit-image effectively addresses their needs. We do this through annual Community Summits, connecting first with known groups---the Advanced Bioimaging Lab (Berkeley) and the Van Valen lab (Caltech)---and then expanding to other groups and individuals.

From these meetings, we derive specific needs, which expand a list of known technical requirements, enumerated below. In response, to discuss and implement solutions, we host annual Developer Summits, which bring together scikit-image developers as well as other ecosystem developers with similar concerns, such as the NiPy, DiPy, Napari, and DeepLabCut developers.

As mentioned above, there are several technical work items known upfront, which form goals 2, 3, and 4, namely:

**Goal 2. Hardware acceleration:** We will make scikit-image competitive on modern hardware by enabling GPU workflows. In discussion with the Array API and Cython authors, we  have formulated a strategy for optimizing scikit-image across hardware platforms, and across both vectorized and non-vectorized classes of algorithms. This will make it possible to process larger images at a much more rapid pace.

**Goal 3. AI-accessible documentation:** We will port our documentation to mystmd, whose machine-readable output lets AI agents better discover and use scikit-image. Together with researchers in the community, we will experiment with automated pipeline construction of bioimaging workflows, improving the library and its documentation wherever necessary to improve success rates.

**Goal 4. Image registration:** As a concrete technical deliverable, we will substantially improve our image-registration support. This functionality is commonly requested by researchers across life science research fields, and we have experimental APIs, suitable across a diverse set of applications such as neuroimaging, microscopy, and cell tracking, that we wish to solidify.

**Goal 5. Structured, AI-assisted maintenance:** We appreciate that we are operating in a rapidly changing technological landscape could be of great benefit, yet also has some clear risks. We wish to explore, and determine patterns for, carefully integrating AI into our maintenance workflows. Our hope is to reduce the maintenance burden of many routine tasks (dependency updates, deprecations, CI failures, security fixes, handling merge conflicts, etc.), while freeing developer time for algorithmic work that requires experience, in-depth field knowledge, and careful deliberation.

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

### Goal 1: Community engagement

**Outcome:** Bioimaging researchers gain access to scikit-image routines that address existing workflow shortcomings.

**Milestones & Deliverables:**

1.1 Host community summit to conduct needs assessment with the Advanced Bioimaging Lab (Berkeley) and the Van Valen Lab (Caltech); publish a prioritized roadmap of candidate routines. [Year 1]

1.2. Host developer summit for scikit-image developers. [Year 1]

1.3 Implement and release solutions to highest priority needs identified in 1.1. [Year 1]

1.4. Hold summit to assess needs asseessment across wider life sciences community. [Year 2]

1.2. Host developer summit that extends to more image processing developers in the community, such as NiPy, DiPy, Napari, and DeepLabCut. [Year 2]

1.5 Implement and release solutions to highest priority needs identified in 1.4. [Year 2]

**Success indicators:**

- Meetings are held and reach out to at least 20–30 people.
- At least 5 major features are added to the library in response to community needs.

---

### Goal 2: Hardware acceleration

**Outcome:** Scientists run scikit-image on GPUs to process large datasets.

**Milestones & Deliverables:**

2.1 Finalize an implementation plan in collaboration with the Array API team and Cython developers. [Year 1]

2.2. Prototype an initial GPU implementation for several different types of algorithms. [Year 1]

2.3. Form a plan, based on the above experience, for bringing scikit-image as near as possible to 100% GPU coverage [Year 2].

2.4. Implement GPU accelerated routines for the majority of the library, focusing on most used functionality and documenting progress & exceptions [Year 2].

**Success indicators:**

- Benchmarks for several highly used scikit-image algorithms show significant performance improvement on GPUs.
- Documentation indicates which functions are accelerated this way.

---

### Goal 3: AI-accessible documentation

**Outcome:** Documentation is ported to mystmd. Coding agents can easily discover and correctly compose scikit-image functions.

**Milestones & Deliverables:**

3.1 Port scikit-image documentation to mystmd. [Year 1]

3.2 Build and test, in collaboration with partners, a few end-to-end reference bioimaging workflows, validated with AI agents. [Year 1-2]

3.3 Address library and documentation gaps surfaced by workflow testing. [Year 2]

**Success indicators:**

- Front page, along with user and reference documentation, is migrated to mystmd.
- Prototype workflows can be auto-generated, correctly, start-to-end.

---

### Goal 4: Image registration

**Outcome:** Researchers in neuroimaging, microscopy, and cell tracking gain access to a single, robust registration implementation in scikit-image.

**Milestones & Deliverables:**

4.1 Complete design of a general registration API covering core use cases across target domains, building on the existing prototype. [Year 1]

4.2 Implement and test core registration algorithms (e.g., rigid, affine, deformable) against reference datasets. [Year 1-2]

4.3 Validate the new registration module against real workflows with partner projects (DiPy, NiPy, Van Valen Lab) across at least two domains. [Year 2]

**Success indicators:**

- General-purpose registration module released.
- Module is adopted in at least two research pipelines of varying modalities.

---

### Goal 5: Structured, AI-assisted maintenance

**Outcome:** Maintainers shift their effort from routine upkeep toward algorithmic work, stabilizing the pace of scikit-image development without a reduction in quality, and without a significant increase in code maintainability & complexity.

**Milestones & Deliverables:**

5.1 In collaboration with colleagues from the scientific Python ecosystem, explore patterns for using AI to systematically reduce the project maintenance backlog. [Year 1]

5.2 Apply identified patterns to reduce the backlog.[Year 1-2]

5.3 Publish skills developed in an open repository. [Year 1-2]

**Success indicators:**

- A measurable reduction in time-to-resolution for routine maintenance issues/PRs, as well as a declining number of open issues.
