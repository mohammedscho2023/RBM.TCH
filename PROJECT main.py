<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>RBM & Knowledge System</title>
  <!-- Bootstrap 5 CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" />
  <style>
    body { background: #f8f9fa; padding-top: 20px; }
    .card { border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .card-header { background: #0d6efd; color: white; font-weight: bold; border-radius: 12px 12px 0 0; }
    .tab-content { padding-top: 20px; }
    pre { background: #e9ecef; padding: 12px; border-radius: 8px; white-space: pre-wrap; word-break: break-all; }
    .spinner-border-sm { width: 1rem; height: 1rem; }
  </style>
</head>
<body>
<div class="container">

  <h1 class="text-center mb-4">📊 RBM & Knowledge Management System</h1>

  <!-- Tabs Navigation -->
  <ul class="nav nav-tabs" id="myTab" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active" id="rbm-tab" data-bs-toggle="tab" data-bs-target="#rbm" type="button" role="tab">RBM Engine</button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="knowledge-tab" data-bs-toggle="tab" data-bs-target="#knowledge" type="button" role="tab">Knowledge</button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="reporting-tab" data-bs-toggle="tab" data-bs-target="#reporting" type="button" role="tab">Reporting & Export</button>
    </li>
  </ul>

  <div class="tab-content" id="myTabContent">

    <!-- ==================== RBM TAB ==================== -->
    <div class="tab-pane fade show active" id="rbm" role="tabpanel">
      <div class="row">
        <div class="col-md-6">
          <div class="card">
            <div class="card-header">Generate RBM Package</div>
            <div class="card-body">
              <form id="rbmForm">
                <div class="mb-3">
                  <label class="form-label">Problem Statement</label>
                  <input type="text" class="form-control" id="problem" value="Low school attendance in rural areas" required>
                </div>
                <div class="mb-3">
                  <label class="form-label">Impact Goal</label>
                  <input type="text" class="form-control" id="impact" value="Improved educational outcomes" required>
                </div>
                <div class="mb-3">
                  <label class="form-label">Sector</label>
                  <select class="form-select" id="sector">
                    <option value="education">Education</option>
                    <option value="health">Health</option>
                    <option value="general">General</option>
                  </select>
                </div>
                <button type="submit" class="btn btn-primary w-100">Generate RBM</button>
              </form>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="card-header">RBM Output</div>
            <div class="card-body">
              <div id="rbmResult"><p class="text-muted">Click "Generate RBM" to see results.</p></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== KNOWLEDGE TAB ==================== -->
    <div class="tab-pane fade" id="knowledge" role="tabpanel">
      <div class="row">
        <div class="col-md-6">
          <!-- Add Lesson -->
          <div class="card">
            <div class="card-header">Add Lesson Learned</div>
            <div class="card-body">
              <form id="lessonForm">
                <div class="mb-2">
                  <input type="number" class="form-control" id="lessonProjectId" placeholder="Project ID" value="1" required>
                </div>
                <div class="mb-2">
                  <input type="text" class="form-control" id="lessonTitle" placeholder="Title" required>
                </div>
                <div class="mb-2">
                  <textarea class="form-control" id="lessonText" placeholder="Lesson" rows="2" required></textarea>
                </div>
                <div class="mb-2">
                  <textarea class="form-control" id="lessonRecommendation" placeholder="Recommendation" rows="2" required></textarea>
                </div>
                <button type="submit" class="btn btn-success w-100">Save Lesson</button>
              </form>
            </div>
          </div>
          <!-- Add Evidence -->
          <div class="card mt-3">
            <div class="card-header">Add Evidence</div>
            <div class="card-body">
              <form id="evidenceForm">
                <div class="mb-2">
                  <input type="text" class="form-control" id="evidenceIndicator" placeholder="Indicator" required>
                </div>
                <div class="mb-2">
                  <input type="text" class="form-control" id="evidenceSource" placeholder="Source" required>
                </div>
                <div class="mb-2">
                  <input type="text" class="form-control" id="evidenceFilePath" placeholder="File path" required>
                </div>
                <button type="submit" class="btn btn-success w-100">Save Evidence</button>
              </form>
            </div>
          </div>
          <!-- Add Decision -->
          <div class="card mt-3">
            <div class="card-header">Log Decision</div>
            <div class="card-body">
              <form id="decisionForm">
                <div class="mb-2">
                  <textarea class="form-control" id="decisionText" placeholder="Decision" rows="2" required></textarea>
                </div>
                <div class="mb-2">
                  <textarea class="form-control" id="decisionRationale" placeholder="Rationale" rows="2" required></textarea>
                </div>
                <div class="mb-2">
                  <input type="text" class="form-control" id="decisionOwner" placeholder="Owner" required>
                </div>
                <button type="submit" class="btn btn-success w-100">Log Decision</button>
              </form>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <!-- List Lessons -->
          <div class="card">
            <div class="card-header">Lessons Learned</div>
            <div class="card-body">
              <button id="loadLessonsBtn" class="btn btn-info w-100 mb-3">Load Lessons</button>
              <div id="lessonsList"><p class="text-muted">Click "Load Lessons" to see stored lessons.</p></div>
            </div>
          </div>
          <!-- Additional Knowledge Operations -->
          <div class="card mt-3">
            <div class="card-header">Knowledge Utilities</div>
            <div class="card-body">
              <button id="classifyBtn" class="btn btn-outline-secondary btn-sm me-2">Classify Lesson (demo)</button>
              <button id="caseStudyBtn" class="btn btn-outline-secondary btn-sm">Generate Case Study (demo)</button>
              <div id="utilResult" class="mt-2"><small class="text-muted">Results will appear here.</small></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ==================== REPORTING TAB ==================== -->
    <div class="tab-pane fade" id="reporting" role="tabpanel">
      <div class="row">
        <div class="col-md-6">
          <div class="card">
            <div class="card-header">Quarterly Report</div>
            <div class="card-body">
              <form id="quarterlyForm">
                <div class="mb-2">
                  <input type="text" class="form-control" id="qOutputs" placeholder="Outputs delivered (comma separated)" value="Training completed, Community meetings">
                </div>
                <div class="mb-2">
                  <input type="text" class="form-control" id="qOutcomes" placeholder="Outcomes progress (comma separated)" value="Improved attendance">
                </div>
                <div class="mb-2">
                  <input type="text" class="form-control" id="qRisks" placeholder="Risks (comma separated)" value="Funding delay">
                </div>
                <div class="mb-2">
                  <input type="text" class="form-control" id="qLessons" placeholder="Lessons (comma separated)" value="Community mobilization improves participation">
                </div>
                <div class="mb-2">
                  <input type="text" class="form-control" id="qNextSteps" placeholder="Next steps (comma separated)" value="Expand outreach">
                </div>
                <button type="submit" class="btn btn-primary w-100">Generate Quarterly Report</button>
              </form>
            </div>
          </div>
          <div class="card mt-3">
            <div class="card-header">Indicator Progress</div>
            <div class="card-body">
              <form id="progressForm" class="row g-2">
                <div class="col-4"><input type="number" class="form-control" id="baseline" placeholder="Baseline" value="0" required></div>
                <div class="col-4"><input type="number" class="form-control" id="current" placeholder="Current" value="40" required></div>
                <div class="col-4"><input type="number" class="form-control" id="target" placeholder="Target" value="80" required></div>
                <div class="col-12"><button type="submit" class="btn btn-info w-100">Calculate Progress</button></div>
              </form>
              <div id="progressResult" class="mt-2"></div>
            </div>
          </div>
          <div class="card mt-3">
            <div class="card-header">Dashboard (demo)</div>
            <div class="card-body">
              <button id="dashboardBtn" class="btn btn-warning w-100">Build Dashboard</button>
              <div id="dashboardResult" class="mt-2"></div>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="card-header">Export Reports</div>
            <div class="card-body">
              <p>Export the current quarterly report to:</p>
              <div class="d-grid gap-2">
                <button id="exportExcelBtn" class="btn btn-success">📊 Export to Excel (logframe)</button>
                <button id="exportWordBtn" class="btn btn-primary">📄 Export to Word (quarterly report)</button>
                <button id="exportPdfBtn" class="btn btn-danger">📕 Export to PDF (donor report)</button>
              </div>
              <hr>
              <div id="exportResult" class="mt-2"><small class="text-muted">Exported files will be saved in the backend folder.</small></div>
            </div>
          </div>
          <div class="card mt-3">
            <div class="card-header">Learning Report</div>
            <div class="card-body">
              <button id="learningReportBtn" class="btn btn-secondary w-100">Generate Learning Report (demo)</button>
              <div id="learningReportResult" class="mt-2"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div><!-- end tab-content -->
</div><!-- container -->

<!-- Bootstrap JS for tabs -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

<script>
// Base API URL
const API_BASE = 'http://localhost:8000';

// Helper to show JSON
function showJson(elementId, data) {
  const el = document.getElementById(elementId);
  if (typeof data === 'object') {
    el.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
  } else {
    el.innerHTML = `<pre>${data}</pre>`;
  }
}

// ========== RBM ==========
document.getElementById('rbmForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const problem = document.getElementById('problem').value;
  const impact = document.getElementById('impact').value;
  const sector = document.getElementById('sector').value;
  const payload = { problem, impact, sector };
  try {
    const res = await fetch(`${API_BASE}/rbm/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    showJson('rbmResult', data);
  } catch (err) {
    showJson('rbmResult', 'Error: ' + err.message);
  }
});

// ========== Knowledge: Lessons ==========
document.getElementById('lessonForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    project_id: parseInt(document.getElementById('lessonProjectId').value),
    title: document.getElementById('lessonTitle').value,
    lesson: document.getElementById('lessonText').value,
    recommendation: document.getElementById('lessonRecommendation').value
  };
  try {
    const res = await fetch(`${API_BASE}/knowledge/lessons`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    alert('Lesson saved!');
    document.getElementById('lessonForm').reset();
  } catch (err) {
    alert('Error: ' + err.message);
  }
});

document.getElementById('loadLessonsBtn').addEventListener('click', async () => {
  try {
    const res = await fetch(`${API_BASE}/knowledge/lessons`);
    const data = await res.json();
    showJson('lessonsList', data);
  } catch (err) {
    showJson('lessonsList', 'Error: ' + err.message);
  }
});

// ========== Knowledge: Evidence ==========
document.getElementById('evidenceForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    indicator: document.getElementById('evidenceIndicator').value,
    source: document.getElementById('evidenceSource').value,
    file_path: document.getElementById('evidenceFilePath').value
  };
  try {
    const res = await fetch(`${API_BASE}/knowledge/evidence`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    alert('Evidence saved!');
    document.getElementById('evidenceForm').reset();
  } catch (err) {
    alert('Error: ' + err.message);
  }
});

// ========== Knowledge: Decisions ==========
document.getElementById('decisionForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    decision: document.getElementById('decisionText').value,
    rationale: document.getElementById('decisionRationale').value,
    owner: document.getElementById('decisionOwner').value
  };
  try {
    const res = await fetch(`${API_BASE}/knowledge/decisions`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    alert('Decision logged!');
    document.getElementById('decisionForm').reset();
  } catch (err) {
    alert('Error: ' + err.message);
  }
});

// ========== Knowledge Utilities ==========
document.getElementById('classifyBtn').addEventListener('click', async () => {
  try {
    const res = await fetch(`${API_BASE}/knowledge/classify-lesson?lesson_text=Community engagement improved participation`, {
      method: 'POST'
    });
    const data = await res.json();
    showJson('utilResult', data);
  } catch (err) {
    showJson('utilResult', 'Error: ' + err.message);
  }
});

document.getElementById('caseStudyBtn').addEventListener('click', async () => {
  const payload = {
    title: 'School Attendance Project',
    problem: 'Low attendance in rural schools',
    solution: 'Community outreach and teacher training',
    results: 'Attendance increased by 30%',
    lesson: 'Community ownership is key'
  };
  try {
    const res = await fetch(`${API_BASE}/knowledge/case-study`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    showJson('utilResult', data);
  } catch (err) {
    showJson('utilResult', 'Error: ' + err.message);
  }
});

// ========== Reporting: Quarterly ==========
document.getElementById('quarterlyForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    outputs: document.getElementById('qOutputs').value.split(',').map(s => s.trim()),
    outcomes: document.getElementById('qOutcomes').value.split(',').map(s => s.trim()),
    risks: document.getElementById('qRisks').value.split(',').map(s => s.trim()),
    lessons: document.getElementById('qLessons').value.split(',').map(s => s.trim()),
    next_steps: document.getElementById('qNextSteps').value.split(',').map(s => s.trim())
  };
  try {
    const res = await fetch(`${API_BASE}/reporting/quarterly`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    showJson('exportResult', data);
  } catch (err) {
    showJson('exportResult', 'Error: ' + err.message);
  }
});

// ========== Reporting: Indicator Progress ==========
document.getElementById('progressForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const baseline = parseInt(document.getElementById('baseline').value);
  const current = parseInt(document.getElementById('current').value);
  const target = parseInt(document.getElementById('target').value);
  try {
    const res = await fetch(`${API_BASE}/reporting/indicator-progress?baseline=${baseline}&current=${current}&target=${target}`, {
      method: 'POST'
    });
    const data = await res.json();
    document.getElementById('progressResult').innerHTML = `<div class="alert alert-info">Progress: ${data.progress}%</div>`;
  } catch (err) {
    document.getElementById('progressResult').innerHTML = `<div class="alert alert-danger">Error: ${err.message}</div>`;
  }
});

// ========== Reporting: Dashboard ==========
document.getElementById('dashboardBtn').addEventListener('click', async () => {
  const sampleIndicators = [
    { indicator: 'Enrollment rate', progress: 75 },
    { indicator: 'Test scores', progress: 45 },
    { indicator: 'Teacher attendance', progress: 90 }
  ];
  try {
    const res = await fetch(`${API_BASE}/reporting/dashboard`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(sampleIndicators)
    });
    const data = await res.json();
    showJson('dashboardResult', data);
  } catch (err) {
    showJson('dashboardResult', 'Error: ' + err.message);
  }
});

// ========== Reporting: Learning Report ==========
document.getElementById('learningReportBtn').addEventListener('click', async () => {
  const sampleLessons = [
    { title: 'Lesson 1', lesson: 'Community engagement works', recommendation: 'Increase community forums' },
    { title: 'Lesson 2', lesson: 'Supply chain fragile', recommendation: 'Pre-position supplies' }
  ];
  try {
    const res = await fetch(`${API_BASE}/reporting/learning-report`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(sampleLessons)
    });
    const data = await res.json();
    showJson('learningReportResult', data);
  } catch (err) {
    showJson('learningReportResult', 'Error: ' + err.message);
  }
});

// ========== Reporting: Exports ==========
async function exportFile(endpoint, payload, filename, method = 'POST') {
  try {
    const res = await fetch(`${API_BASE}${endpoint}`, {
      method: method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    showJson('exportResult', data);
  } catch (err) {
    showJson('exportResult', 'Error: ' + err.message);
  }
}

document.getElementById('exportExcelBtn').addEventListener('click', async () => {
  // We need some logframe data; we can generate a dummy one or ask the user.
  // For simplicity, we'll use a static logframe.
  const logframe = [
    { level: 'Impact', statement: 'Improved education', indicator: 'Pass rate', baseline: 50, target: 80 },
    { level: 'Outcome', statement: 'Better teacher skills', indicator: 'Training completion', baseline: 0, target: 100 }
  ];
  await exportFile('/reporting/export-excel?filename=logframe.xlsx', logframe);
});

document.getElementById('exportWordBtn').addEventListener('click', async () => {
  const report = {
    executive_summary: 'Good progress this quarter',
    outputs_delivered: ['Training done', 'Materials distributed'],
    outcomes_progress: ['Attendance up by 10%'],
    risks: ['None significant'],
    lessons: ['Community engagement helps'],
    next_steps: ['Continue advocacy']
  };
  await exportFile('/reporting/export-word?filename=quarterly.docx', report);
});

document.getElementById('exportPdfBtn').addEventListener('click', async () => {
  const donorReport = {
    'Executive Summary': 'Project on track',
    'Theory of Change': 'If we train teachers, then learning improves',
    'Results': '80% of schools have trained teachers',
    'Budget': 'Within 5% of plan'
  };
  await exportFile('/reporting/export-pdf?filename=donor_report.pdf', donorReport);
});

</script>
</body>
</html>
