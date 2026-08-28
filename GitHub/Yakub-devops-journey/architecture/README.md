# Architecture diagrams

One diagram per lab, plus the capstone. Draw them yourself — draw.io, Excalidraw, or
paper and a phone camera. A diagram you copied teaches you nothing.

| File | Lab | Status |
|---|---|---|
| `lab-01.png` | Lift & Shift on EC2 | [ ] |
| `lab-02.png` | Jenkins CI pipeline flow | [ ] |
| `lab-03.png` | GitHub Actions / GitLab pipelines | [ ] |
| `lab-04.png` | Terraform-managed infrastructure | [ ] |
| `lab-05.png` | Ansible + monitoring stack | [ ] |
| `lab-06.png` | Three-tier VPC | [ ] |
| `lab-07.png` | Containerized stack | [ ] |
| `lab-08.png` | Kubernetes deployment | [ ] |
| `capstone.png` | Full GitOps pipeline | [ ] |

## What a good diagram shows

- Every component, named as it is actually named in your code
- The direction of traffic, with protocols and ports
- Trust boundaries — what is public, what is private
- Where secrets come from

If a reviewer has to ask "how does the app find the database?", the diagram is incomplete.
