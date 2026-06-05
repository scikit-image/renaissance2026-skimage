# scikit-image (https://scikit-image.org) proposal ideation

- PI: Stéfan van der Walt at BIDS; University of California, Berkeley

We are doing the 1M foundation library track.

## Project goals

This proposal is centered around expanding and improving the use of scikit-image in life science imaging.

The team have spent significant effort on an skimage 2.0 API—a healthy development, which modernizes our API, brings all functions in line with best practices, makes the library more uniform and implements skimage design protocols across the board.
However, this also means that, for several years now, we have been focused predominantly on refactoring, API design, and software engineering mechanics (CI, testing, etc.).
It is time for us to return to our users, and to improve and expand the library for their benefit.

With this funding, we intend to:

#. Connect to the bioimaging community, learn about their needs, and implement those needs.
   Specifically, we are intending to talk to the NiPy & DiPy teams, the Vanvalen lab at Caltech, the Advanced Bioimaging Center at Berkeley, and the Napari developers.
   We are open to engaging with other groups too, as opportunities present themselves.
#. Make the library competitive on modern hardware, by enabling GPU workflows.
   The Array API is currently being rolled out across the ecosystem, but is insufficient to address this need for project that are prodominantly Cython based.
   We are planning to coordinate with the Cython team, as well as to explore other technological pathways to make that happen.
#. Improve our library documentation to be better machine-accessible, so that skimage may be integrated more closely in AI workflows.
   We intend to port all of our documentation to mystmd, which has machine readable JSON output.
   We also want to trial setting up end-to-end bioimaging workflows, and change what we can at the library and documentation level to improve those workflows.
#. Specific technical aim: while we will learn from our bioimaging collaborators about their needs, one specific feature we would like to implement and roll out is image registration. We have some basic support, and an initial API, but we can drastically expand that offering. This should be useful to others in neuroimaging, microscopy, and many other sub-fields of life sciences.
#. We'd need to continue performing some maintenance, but it'd be a different flavor than before: currently, we use AI fairly haphazardly, in an unstructured ad-hoc way to address maintenance issues. We will integrate AI more closely, in a structured way, into our maintenance workflows to handle many routine tasks (dependency updates, integrating community best practices, security updates, and handling of deprecations, CI failures, and test updates). By freeing up developer time, we hope to drastically reduce the maintenance backlog and be able to focus more on algorithmic improvements.

## CVs

### Stéfan

- Founder scikit-image, co-founder Scientific Python
- Core team member: NumPy, SciPy, scikit-image, NetworkX, Jupyter Book

I will be the PI on this proposal. I founded the library, as well as co-founded the Scientific Python coordinating project. I have a long history in the ecosystem, and developing several libraries, including bioimaging libraries like DiPy (I was a core developer for two years). My background is in Applied Mathematics with a focus on image processing, and I am the co-creator of the ubiquitous Viridis colormap.
