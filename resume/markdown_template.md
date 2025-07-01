Title: Resume
Slug: resume

<div class="content resume-content">
  <div class="resume-header">
    <h1>{{ basics.name }}</h1>
    <div class="contact-info">
      <p>{{ basics.location.city }}</p>
      <p><a href="mailto:{{ basics.email }}">{{ basics.email }}</a></p>
      <p><a href="{{ basics.url }}">{{ basics.url }}</a></p>
      <p><strong><a href="/downloads/resume.pdf">Download PDF</a></strong></p>
    </div>
  </div>

  <section class="summary">
    <h2>Summary</h2>
    {{ basics.summary | md }}
  </section>

  <section class="work-history">
    <h2>Work History</h2>
    {% for job in work %}
    <div class="job">
      <div class="job-header">
        <h3>{{ job.name }}</h3>
        <span class="dates">{{ job | date_range }}</span>
      </div>
      <div class="position">{{ job.position }}</div>
      <div class="job-summary">{{ job.summary | md }}</div>
    </div>
    {% endfor %}
  </section>

  <section class="projects">
    <h2>Personal Projects</h2>
    {% for project in projects %}
    <div class="project">
      <div class="project-header">
        <h3><a href="{{ project.url }}">{{ project.name }}</a></h3>
        <span class="dates">{{ project | date_range }}</span>
      </div>
      <div class="project-description">{{ project.description | md }}</div>
    </div>
    {% endfor %}
  </section>

  <section class="education">
    <h2>Education</h2>
    {% for edu in education %}
    <div class="education-item">
      <div class="education-header">
        <h3>{{ edu.institution }}</h3>
        <span class="dates">{{ edu | date_range }}</span>
      </div>
      <div class="degree">{{ edu.studyType }} in {{ edu.area }}</div>
      <div class="education-summary">{{ edu.summary | md }}</div>
    </div>
    {% endfor %}
  </section>

  <section class="skills">
    <h2>Skills</h2>
    {% for skill in skills %}
    <div class="skill-group">
      <h4>{{ skill.name }}</h4>
      <div class="skill-keywords">{{ skill.keywords | comma_list }}</div>
      {% if skill.text %}
      <div class="skill-text">{{ skill.text | md }}</div>
      {% endif %}
    </div>
    {% endfor %}
  </section>

  {% for appendix in appendices %}
  <section class="appendix">
    <h2>{{ appendix.title }}</h2>
    <div class="appendix-content">{{ appendix.text | md }}</div>
  </section>
  {% endfor %}
</div>

<style>
.resume-content {
  max-width: 800px;
  margin: 0 auto;
}

.resume-header {
  text-align: center;
  margin-bottom: var(--space-8);
  border-bottom: 2px solid var(--gray-9);
  padding-bottom: var(--space-6);
}

.resume-header h1 {
  font-size: var(--font-size-3xl);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--space-4);
  color: var(--text-primary);
}

.contact-info p {
  margin: var(--space-1) 0;
  color: var(--text-secondary);
}

.resume-content section {
  margin-bottom: var(--space-8);
}

.resume-content h2 {
  font-size: var(--font-size-xl);
  font-weight: var(--font-weight-semibold);
  color: var(--accent-primary);
  border-bottom: 1px solid var(--gray-9);
  padding-bottom: var(--space-2);
  margin-bottom: var(--space-6);
}

.job, .project, .education-item {
  margin-bottom: var(--space-6);
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--gray-11);
}

.job:last-child, .project:last-child, .education-item:last-child {
  border-bottom: none;
}

.job-header, .project-header, .education-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: var(--space-2);
}

.job-header h3, .project-header h3, .education-header h3 {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-medium);
  color: var(--text-primary);
  margin: 0;
}

.dates {
  font-size: var(--font-size-sm);
  color: var(--text-muted);
  font-weight: var(--font-weight-normal);
}

.position, .degree {
  font-size: var(--font-size-base);
  color: var(--text-secondary);
  font-style: italic;
  margin-bottom: var(--space-3);
}

.job-summary, .project-description, .education-summary {
  color: var(--text-secondary);
  line-height: 1.6;
}

.skill-group {
  margin-bottom: var(--space-4);
}

.skill-group h4 {
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  color: var(--text-primary);
  margin-bottom: var(--space-2);
}

.skill-keywords {
  color: var(--text-secondary);
  line-height: 1.6;
}

.skill-text {
  margin-top: var(--space-2);
  color: var(--text-muted);
  font-size: var(--font-size-sm);
}

.appendix-content {
  color: var(--text-secondary);
  line-height: 1.6;
}

@media (max-width: 768px) {
  .job-header, .project-header, .education-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .dates {
    margin-top: var(--space-1);
  }
}
</style>