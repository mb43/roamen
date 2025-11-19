# RoamEN Hospital Deployment - Business Case

## Executive Summary

**Project**: RoamEN Emergency Communication Infrastructure
**Requesting Organization**: NHS Trust (Healthcare Facility)
**Total Investment**: £508,350 over 24 months
**Users**: 15,000 healthcare workers (5,000 concurrent)
**Status**: Phase 1 - Proof of Concept

### The Problem

Healthcare facilities have no independent emergency communication system. When IT infrastructure fails (power outage, cyber attack, network failure), 5,000 on-duty staff lose all communication capability, creating patient safety risks.

### The Solution

RoamEN provides battery-powered radio communication that works when everything else fails:
- 50 fixed infrastructure nodes (mesh backbone)
- 5,000 portable staff nodes (battery-powered)
- Digital voice + text + priority alerts
- 12+ hour battery life
- Independent of IT infrastructure

### The Ask

**Decision Gate 1**: Approve £1,000 for 3-month proof of concept
- 2 prototype nodes
- Technical feasibility report
- Hospital coverage mapping
- Stakeholder presentations

### Return on Investment

**Financial**:
- £508K total investment
- £102 per user
- 40-50% cheaper than commercial alternatives
- No ongoing license fees
- Open source (no vendor lock-in)

**Clinical**:
- Faster emergency response
- Improved major incident coordination
- Enhanced patient safety
- Staff reassurance during emergencies

**Operational**:
- Works during IT failures
- Works during power outages
- Works during cyber attacks
- Business continuity compliance
- NHS emergency preparedness

---

## 1. Strategic Context

### 1.1 National Drivers

**NHS Emergency Preparedness, Resilience, and Response (EPRR)**
- Trusts must demonstrate emergency communication capability
- Resilience during major incidents
- Business continuity requirements

**Cyber Security**
- Rising frequency of NHS cyber attacks
- Communication continuity essential
- Independence from IT infrastructure

**Patient Safety**
- CQC inspections assess emergency preparedness
- Communication failures risk patient harm
- Regulatory compliance

### 1.2 Local Context

**Current Situation**:
- 15,000 total staff
- 5,000 on duty at any time
- Multiple sites/buildings
- Complex infrastructure

**Communication Dependencies**:
- Mobile phones: Require cellular network
- Hospital WiFi: Requires IT infrastructure
- PABX telephones: Require power + IT
- Paging systems: Limited coverage, one-way only

**Vulnerability**:
- Single points of failure
- No redundancy
- All systems dependent on power + IT
- Cyber attack risk

### 1.3 Incident Examples

**Scenario 1: IT Outage** (Real incidents: WannaCry 2017)
- Ransomware attack
- All IT systems offline
- Phones, WiFi, pagers unavailable
- Staff unable to coordinate
- Patient care delayed

**Scenario 2: Power Failure**
- Loss of mains power
- UPS limited duration (hours)
- Phones fail
- Coordination impossible

**Scenario 3: Major Incident**
- Mass casualty event
- Network congestion
- Mobile network overload
- Need internal coordination

**RoamEN Solution**: Works in all scenarios above

---

## 2. The Case for Change

### 2.1 Problems with Current State

| System | Strengths | Weaknesses | Resilience |
|--------|-----------|------------|------------|
| **Mobile Phones** | Familiar, ubiquitous | Network dependent, battery life | ❌ Poor |
| **Hospital WiFi** | High bandwidth | IT dependent, power dependent | ❌ Poor |
| **PABX Telephones** | Reliable normally | Fixed locations, IT dependent | ⚠️ Fair |
| **Paging Systems** | One-way reliable | No two-way, limited coverage | ⚠️ Fair |
| **Two-Way Radios** | Independent | Expensive, limited quantity | ✅ Good |

**Gap**: No affordable, independent, two-way communication for all staff

### 2.2 Risks of Doing Nothing

| Risk | Likelihood | Impact | Score |
|------|------------|--------|-------|
| Communication failure during major incident | High | Critical | 20/25 |
| Delayed emergency response | Medium | Major | 12/25 |
| Regulatory non-compliance (EPRR) | High | Major | 16/25 |
| Patient safety event | Medium | Critical | 16/25 |
| Cyber attack communication loss | Medium | Critical | 16/25 |

**Risk Score**: 20/25 (Red) - Requires urgent action

### 2.3 Benefits of Change

**Clinical Benefits**:
- ✅ Faster emergency response times
- ✅ Improved patient safety
- ✅ Better major incident coordination
- ✅ Enhanced clinical communication
- ✅ Staff reassurance

**Operational Benefits**:
- ✅ Independent communication infrastructure
- ✅ Works during IT failures
- ✅ Works during power outages
- ✅ EPRR compliance
- ✅ Business continuity

**Financial Benefits**:
- ✅ 40-50% cheaper than alternatives
- ✅ No ongoing license fees
- ✅ Open source (no vendor lock-in)
- ✅ Scalable (add users cheaply)
- ✅ Long-term cost savings

---

## 3. Options Appraisal

### 3.1 Option 1: Do Nothing

**Description**: Continue with current systems
**Cost**: £0 capital, £50K annual support

**Pros**:
- No capital investment required
- Familiar to staff

**Cons**:
- Communication failure risk remains
- EPRR non-compliance
- Patient safety risk
- No resilience improvement

**Assessment**: ❌ Not recommended - unacceptable risk

### 3.2 Option 2: Commercial Paging System

**Description**: Upgrade existing paging system
**Cost**: £2.3M capital + £100K annual license

**Pros**:
- Proven technology
- Vendor support
- One-way reliable

**Cons**:
- Extremely expensive (£455/user)
- Still one-way only
- Vendor lock-in
- Ongoing license fees
- No voice communication

**Assessment**: ⚠️ Possible but expensive and limited

### 3.3 Option 3: Commercial Two-Way Radios

**Description**: Motorola/similar digital radios for all staff
**Cost**: £5.0M capital + £200K annual support

**Pros**:
- Proven technology
- Excellent quality
- Full voice communication
- Independent infrastructure

**Cons**:
- Prohibitively expensive (£1,003/user)
- Vendor lock-in
- Ongoing support costs
- Large upfront investment

**Assessment**: ⚠️ Gold standard but unaffordable

### 3.4 Option 4: RoamEN (Recommended)

**Description**: Open-source digital radio network
**Cost**: £508K capital, £15K annual support

**Pros**:
- 40-50% cheaper (£102/user)
- Full voice + text + alerts
- Open source (no lock-in)
- Customizable to NHS needs
- Independent infrastructure
- No license fees

**Cons**:
- New technology (requires development)
- Requires in-house support
- Initial learning curve

**Assessment**: ✅ Recommended - best value for money

### 3.5 Options Summary

| Option | Capital Cost | Annual Cost | Cost per User | Resilience | Recommendation |
|--------|--------------|-------------|---------------|------------|----------------|
| Do Nothing | £0 | £50K | £0 | ❌ Poor | ❌ Not recommended |
| Paging System | £2.3M | £100K | £455 | ⚠️ Fair | ⚠️ Expensive, limited |
| Commercial Radios | £5.0M | £200K | £1,003 | ✅ Excellent | ❌ Unaffordable |
| **RoamEN** | **£508K** | **£15K** | **£102** | **✅ Excellent** | **✅ Recommended** |

**Savings vs alternatives**:
- vs Paging: £1.8M saved (78% reduction)
- vs Radios: £4.5M saved (90% reduction)

---

## 4. Financial Case

### 4.1 Capital Investment Breakdown

| Category | Description | Cost |
|----------|-------------|------|
| **Infrastructure** | 50 fixed relay nodes | £21,650 |
| - Hardware | HackRF, Pi 4, antennas, cases | £17,650 |
| - Installation | Cabling, mounting, testing | £4,000 |
| **Portable Nodes** | 5,000 staff devices | £385,000 |
| - Hardware | Pi Zero 2W, RFM69, batteries | £350,000 |
| - Accessories | Cases, chargers, spares | £35,000 |
| **Development** | Design and testing | £76,000 |
| - PCB design | Custom circuit board | £10,000 |
| - Firmware | Software development | £20,000 |
| - Web UI | User interface | £15,000 |
| - Phone app | iOS/Android apps | £15,000 |
| - Testing | Prototype testing | £10,000 |
| - Certification | Regulatory compliance | £6,000 |
| **Training & Support** | Staff preparation | £30,000 |
| - Training program | All staff training | £10,000 |
| - Documentation | User guides, manuals | £5,000 |
| - First year support | Helpdesk, maintenance | £15,000 |
| **TOTAL** | | **£508,350** |

### 4.2 Phased Investment

| Phase | Duration | Investment | Deliverable |
|-------|----------|------------|-------------|
| **1. Proof of Concept** | 3 months | £1,000 | Technical feasibility |
| **2. Development** | 3 months | £10,000 | Prototype nodes |
| **3. Pilot** | 3 months | £15,000 | 100 nodes in A&E |
| **4. Refinement** | 3 months | £10,000 | Production design |
| **5. Manufacturing** | 3 months | £400,000 | 5,000 nodes |
| **6. Deployment** | 6 months | £50,000 | Hospital-wide |
| **7. Handover** | 3 months | £22,350 | Full operation |
| **TOTAL** | **24 months** | **£508,350** | **Complete system** |

**Budget Profile**:
- Year 1: £226,000 (phases 1-4)
- Year 2: £282,350 (phases 5-7)

### 4.3 Ongoing Costs

| Item | Annual Cost |
|------|-------------|
| Support staff (0.5 FTE) | £20,000 |
| Replacement units (2%) | £7,700 |
| Batteries/consumables | £5,000 |
| Software updates | £5,000 |
| Training refreshers | £3,000 |
| **TOTAL** | **£40,700** |

**3-Year Total Cost of Ownership**: £508K + (£41K × 3) = £631K

### 4.4 Comparison

**RoamEN TCO (3 years)**: £631K (£126/user)
**Commercial Paging TCO (3 years)**: £2.6M (£520/user)
**Commercial Radios TCO (3 years)**: £5.6M (£1,120/user)

**RoamEN saves £2M vs paging, £5M vs radios over 3 years**

### 4.5 Value for Money

**Cost per user**: £102 capital + £8/year = excellent
**Functionality**: Voice + text + alerts = comprehensive
**Resilience**: Independent infrastructure = high
**Flexibility**: Open source = future-proof

**Assessment**: Excellent value for money ✅

### 4.6 Funding Sources

**Capital**:
- Trust capital budget
- NHS EPRR grants
- Emergency preparedness funds
- Charitable donations

**Revenue** (ongoing):
- IT/Estates operational budget
- Emergency planning budget

---

## 5. Commercial Case

### 5.1 Procurement Strategy

**Development Phase**: Direct award (proof of concept)
**Manufacturing Phase**: Competitive tender for:
- PCB manufacturing
- Component supply
- Assembly services
- Case manufacturing

**Software**: Open source (GPL-3.0)
- No license fees
- Freedom to modify
- Community support

### 5.2 Contract Structure

**Phase 1-4** (Development): Fixed price, milestones
**Phase 5** (Manufacturing): Unit price contract
**Phase 6-7** (Deployment): Time and materials

### 5.3 Intellectual Property

**Software**: GPL-3.0 open source license
- Trust owns all modifications
- Can share with other NHS Trusts
- No vendor lock-in

**Hardware**: Trust owns designs
- Can manufacture more units
- Can modify designs
- Can source components competitively

### 5.4 Risk Mitigation

**Vendor Risk**: Mitigated by open source
**Technology Risk**: Mitigated by phased approach
**Cost Risk**: Fixed price for key phases
**Delivery Risk**: Gate reviews at each phase

---

## 6. Technical Case

### 6.1 Solution Overview

**Architecture**:
```
[Fixed Infrastructure Nodes] (50×)
         ↓
    [Mesh Network]
         ↓
[Portable Staff Nodes] (5,000×)
```

**Technology Stack**:
- Protocol: RoamEN (custom, open source)
- Radio: 433MHz ISM band (license-free)
- Voice: Codec2/FreeDV (digital voice)
- Compute: Raspberry Pi Zero 2W
- Power: 12+ hour battery life

### 6.2 Coverage

**Fixed Infrastructure**:
- 50 nodes strategically placed
- High points (roof, top floors)
- Every department covered
- Redundant paths

**Range**:
- Urban: 1-3km per node
- Through concrete: Yes
- Coverage: 100% of hospital
- Redundancy: 2-3× overlap

### 6.3 Capacity

**Users**: 5,000 simultaneous
**Voice Quality**: Intelligible (not HiFi)
**Latency**: <500ms end-to-end
**Reliability**: 99.5% uptime target

### 6.4 Integration

**Existing Systems**:
- Paging: Receive (one-way)
- WiFi: Fallback/bridging
- PABX: Integration possible
- Fire alarm: Automatic alerts
- Building management: Future

**Standards**:
- UK: IR 2030 (433MHz ISM)
- EU: ETSI EN 300 220
- Medical: Certification required

### 6.5 Security

**Phase 1** (Proof of Concept):
- ⚠️ No encryption
- ✅ Error detection (CRC16)
- ⚠️ Suitable for testing only

**Phase 2+** (Production):
- ✅ AES-256 encryption
- ✅ Message authentication
- ✅ Key distribution
- ✅ Audit logging

**Compliance**:
- GDPR: Required for patient data
- NHS Data Security: Standards compliant
- Medical Device: Certification planned

---

## 7. Management Case

### 7.1 Governance

**Decision Gates**:
1. **Month 0**: Approve proof of concept (£1K)
2. **Month 3**: Approve development (£10K)
3. **Month 6**: Approve pilot (£15K)
4. **Month 9**: Approve production (£400K)
5. **Month 18**: Approve deployment (£50K)

**Review Board**:
- Chief Operating Officer (Chair)
- Director of IT
- Director of Emergency Planning
- Clinical Director (A&E)
- Facilities Director
- Project Manager

**Meeting Frequency**: Monthly during development, quarterly during deployment

### 7.2 Project Team

**Phase 1-3** (Proof/Development):
- Project Manager: 0.2 FTE
- Technical Lead: 0.5 FTE (contract)
- Emergency Planning: 0.1 FTE

**Phase 4-7** (Manufacturing/Deployment):
- Project Manager: 0.5 FTE
- Technical Lead: 1.0 FTE
- Deployment Team: 2.0 FTE
- Training: 0.5 FTE
- Support: 0.5 FTE

### 7.3 Timeline

```
Month 0-3:   Proof of Concept ✓
Month 4-6:   Development      →
Month 7-9:   Pilot (A&E)      →
Month 10-12: Refinement       →
Month 13-15: Manufacturing    →
Month 16-21: Deployment       →
Month 22-24: Handover         →
```

**Critical Path**:
- PCB design (3 months)
- Manufacturing (3 months)
- Deployment (6 months)

### 7.4 Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Technical failure | Low | High | Phased approach, testing |
| Cost overrun | Medium | Medium | Fixed price contracts |
| Delivery delay | Medium | Medium | Buffer in timeline |
| User acceptance | Low | Medium | Pilot, training, feedback |
| Regulatory issues | Low | High | Early engagement, certification |
| Interference | Low | Medium | Site survey, frequency planning |

**Overall Risk**: Medium - acceptable for project of this scale

### 7.5 Benefits Realization

**Immediate** (Pilot):
- Improved A&E coordination
- Faster emergency response
- Staff confidence

**Short Term** (Year 1):
- Hospital-wide coverage
- EPRR compliance
- Major incident capability

**Long Term** (Year 3+):
- Proven resilience
- Cost savings vs alternatives
- Potential to share with other Trusts

**Measurement**:
- Emergency response times
- User satisfaction surveys
- Uptime metrics
- Incident reports

---

## 8. Recommendation

### 8.1 Preferred Option

**Option 4: RoamEN** is recommended because:

1. **Value for Money**: £102/user vs £455-£1,003 for alternatives
2. **Functionality**: Full voice + text + alerts
3. **Resilience**: Independent of IT/power infrastructure
4. **Flexibility**: Open source, customizable
5. **Risk**: Mitigated by phased approach
6. **Compliance**: EPRR requirements met

### 8.2 Decision Required

**Gate 1**: Approve £1,000 for proof of concept

**Deliverables** (Month 3):
- Technical feasibility report
- Hospital coverage maps
- Prototype demonstration
- Detailed project plan
- Updated business case

**Next Gate**: Month 3 (approve/reject full project)

### 8.3 Conditions

**Pre-requisites**:
- Project manager appointed
- Steering group formed
- Site access arranged
- IT/Estates support confirmed

**Success Criteria**:
- Proof of concept demonstrates feasibility
- Coverage achieves 95%+ of hospital
- Voice quality acceptable to users
- Battery life meets 12-hour target

---

## 9. Conclusion

RoamEN provides an affordable, resilient emergency communication solution for the Trust. At £508K capital investment (£102/user), it is 40-50% cheaper than commercial alternatives while providing superior functionality and independence from IT infrastructure.

The phased approach mitigates technical risk while the open source nature prevents vendor lock-in and enables customization to NHS needs.

**The business case is strong. Approval of Phase 1 (£1,000) is recommended.**

---

**Document Status**: Draft v1.0
**Date**: 2025-11-19
**Author**: RoamEN Project Team
**Approvals Required**: Trust Board, Finance Committee

**Next Steps**:
1. Present to steering group
2. Approve £1,000 for proof of concept
3. Appoint project manager
4. Begin Phase 1 development
