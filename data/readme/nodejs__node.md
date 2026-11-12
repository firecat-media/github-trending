# Node.js

Node.js is an open-source, cross-platform JavaScript runtime environment.

For information on using Node.js, see the [Node.js website][].

The Node.js project uses an [open governance model](./GOVERNANCE.md). The
[OpenJS Foundation][] provides support for the project.

Contributors are expected to act in a collaborative manner to move
the project forward. We encourage the constructive exchange of contrary
opinions and compromise. The [TSC](./GOVERNANCE.md#technical-steering-committee)
reserves the right to limit or block contributors who repeatedly act in ways
that discourage, exhaust, or otherwise negatively affect other participants.

**This project has a [Code of Conduct][].**

## Table of contents

* [Support](#support)
* [Release types](#release-types)
  * [Download](#download)
    * [Current and LTS releases](#current-and-lts-releases)
    * [Nightly releases](#nightly-releases)
    * [API documentation](#api-documentation)
  * [Verifying binaries](#verifying-binaries)
* [Building Node.js](#building-nodejs)
* [Security](#security)
* [Contributing to Node.js](#contributing-to-nodejs)
* [Current project team members](#current-project-team-members)
  * [TSC (Technical Steering Committee)](#tsc-technical-steering-committee)
  * [Collaborators](#collaborators)
  * [Triagers](#triagers)
  * [Release keys](#release-keys)
* [License](#license)

## Support

Looking for help? Check out the
[instructions for getting support](.github/SUPPORT.md).

## Release types

Node.js follows [semantic versioning](https://semver.org).

* **Alpha**: Under active development where semver-major changes are allowed.
  Each October, a new release line (for example, Node.js 27) branches off `main`
  and receives Alpha releases (for example, `27.0.0-alpha.0.0.0`) for 6 months,
  then are promoted to Current (see below) each April. Alpha releases are signed,
  tagged, and tested through [CITGM](https://github.com/nodejs/citgm), but their
  API and ABI may change between releases. They are intended for library authors
  and CI pipelines, not for production use.
* **Current**: Under active development, no semver-major changes allowed. Node.js
  releases a new major version once a year, in April. Releases stay Current for
  6 months, then convert to LTS (see below) each October. Their ABI may change
  between releases. They are intended for library authors and CI pipelines, not
  for production use.
* **LTS**: Releases under Long Term Support, with a focus on stability
  and security. Only changes that have been on Alpha or Current release for two
  weeks can be backported to a typical LTS release. Every major version becomes an LTS
  release, and receives 30 months of LTS support, for a total of 36 months from
  its first Current release to End-of-Life. LTS release lines have alphabetically-ordered
  code names, beginning with Node.js 4 Argon.
* **Nightly**: Code from the `main` branch built every 24-hours when there are
  changes. Unlike Alpha releases, nightly 
