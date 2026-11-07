# NVIDIA Kubernetes Engine (NVKE)

[ ](LICENSE)
[ ](go.work)

**Run a managed Kubernetes service on your own NVIDIA GPU infrastructure.**
NVIDIA Kubernetes® Engine (NVKE) provides the management plane that platform teams install to create and
operate Kubernetes clusters for their customers. Each workload cluster has its
own Kubernetes control plane, etcd and node pools. You operate the NVKE management
plane; your customers use their clusters through the Kubernetes API and `kubectl`.

> **Preview:** NVKE is available as a preview. APIs, configuration and behavior
> can change between releases, and we do not recommend NVKE for production
> workloads. See [Preview status and known limitations](docs/overview/preview-status.md).

[Get started](#getting-started) · [Documentation](docs/README.md) ·
[Contribute](CONTRIBUTING.md) · [Get help](SUPPORT.md)

## Getting started

| Your goal | Start here | What you get |
|---|---|---|
| **Evaluate without GPU hardware** | [Local quickstart](docs/get-started/quickstart-local.md) | A development management plane and a workload cluster on simulated machines. No NVIDIA account is required. |
| **Install on your infrastructure** | [Plan your installation](docs/operate/plan-installation.md) | The prerequisites and sequence for preparing nodes, bootstrapping a management cluster and installing its services. |
| **Build or contribute** | [Build from source](#build-from-source) | The NVKE binaries and the contributor development loop. |

The local quickstart runs on a **Linux host or VM, amd64 or arm64**, with at least
**6 CPUs, 12 GiB of free memory and 100 GiB of free disk**. It requires Docker,
virtual TPM support and the tools listed in the guide. Follow its setup through
workload-cluster creation and confirm the cluster's nodes report `Ready`.
On macOS, use the [local site guide](docs/get-started/local-site.md), which runs
the evaluation inside a Colima virtual machine.

For a real installation, you supply the machines, networking, node images and
registries, and configure access to **NVIDIA Infra Controller (NICo)**. NICo is
the sole compatible infrastructure provider at preview. The
[platform and version reference](docs/overview/supported-platforms.md) lists
validated combinations and pinned dependencies.

## What NVKE does

- **Creates independent workload clusters.** Request clusters through the NVKE
  API or `nvkectl`; NVKE provisions machines through NICo and forms Kubernetes
  clusters with their own control planes.
- **Manages workload cluster lifecycle.** Create, scale and delete node pools,
  upgrade Kubernetes and replace nodes. See the [node pool guide](docs/workload-clusters/node-pools.md)
  for the manual steps and preview limits on replacement and upgrades.
- **Establishes node identity.** Nodes attest through SPIFFE/SPIRE using their
  TPM before receiving join credentials. Encryption of etcd data is available
  per cluster.
- **Connects builds to deployment.** Its companion project,
  [NVIDIA Kube
