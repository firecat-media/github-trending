Prometheus

 Visit  prometheus.io  for the full documentation,
examples and guides. 

[ ](https://github.com/prometheus/prometheus/actions/workflows/ci.yml)
[ ][quay]
[ ][hub]
[ ](https://bestpractices.coreinfrastructure.org/projects/486)
[ ](https://github.com/prometheus/prometheus/actions/workflows/govulncheck.yml)
[ ](https://securityscorecards.dev/viewer/?uri=github.com/prometheus/prometheus)
[ ](https://clomonitor.io/projects/cncf/prometheus)
[ ](https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=-opened&can=1&q=proj:prometheus)

Prometheus, a [Cloud Native Computing Foundation](https://cncf.io/) project, is a systems and service monitoring system. It collects metrics
from configured targets at given intervals, evaluates rule expressions,
displays the results, and can trigger alerts when specified conditions are observed.

The features that distinguish Prometheus from other metrics and monitoring systems are:

* A **multi-dimensional** data model (time series defined by metric name and set of key/value dimensions)
* PromQL, a **powerful and flexible query language** to leverage this dimensionality
* No dependency on distributed storage; **single server nodes are autonomous**
* An HTTP **pull model** for time series collection
* **Pushing time series** is supported via an intermediary gateway for batch jobs
* Targets are discovered via **service discovery** or **static configuration**
* Multiple modes of **graphing and dashboarding support**
* Support for hierarchical and horizontal **federation**

## Architecture overview

## Install

There are various ways to install Prometheus.

### Precompiled binaries

Precompiled binaries for released versions are available in the
[*download* section](https://prometheus.io/download/)
on [prometheus.io](https://prometheus.io). Using the latest production release binary
is the recommended way to install Prometheus.
See the [Installing](https://prometheus.io/docs/introduction/install/)
chapter in the documentation for all the details.

### Docker images

Docker images are available on [Quay.io](https://quay.io/repository/prometheus/prometheus) or [Docker Hub](https://hub.docker.com/r/prom/prometheus/).

You can launch a Prometheus container for trying it out with

```bash
docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus
```

Prometheus will now be reachable at  .

### Building from source

To build Prometheus from source code, you need:

* Go: Version specified in [go.mod](./go.mod) or greater.
* NodeJS: Version specified in [.nvmrc](./web/ui/.nvmrc) or greater.
* npm: Version 10 or greater (check with `npm --version` and [here](https://www.npmjs.com/)).

Start by cloning the repository:

```bash
git clone https://github.com/prometheus/prometheus.git
cd prometheus
```

You can use the `go` tool to build and install the `prometheus`
and `promtool` binaries into your `GOPATH`:

```bash
go install github.com/prometheus/prometheus/cmd/...
prometheus --config.file=your_config.yml
```

*
