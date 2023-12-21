<h1>Project</h1>
<p>	&nbsp;	&nbsp;	&nbsp;	&nbsp;In this projeact, You can view my blog, what I have posted but you can not change anything.</p>

<h1>Requirements</h1>
<ul>
    <li>Python(version 3 or above)</li>
    <li>IDLE - Choose what you want, I used VSCode</li>
    <li>Here I uesd Flask framework</li>
    <li>PyMySQL module is used to connect Flask and MySQL</li>
</ul>

<h1>Flask</h1>
<p>	&nbsp;	&nbsp;	&nbsp;	&nbsp;Flask is a lightweight and versatile web framework written in Python. It's known for its simplicity, flexibility, and ease of use, making it a popular choice for building web applications, APIs, and other web-related projects.</p>
<p>Key aspects and features of Flask:</p>
<ol>
    <li><b>Micro-framework:</b> Flask is a micro-framework, meaning it's minimalistic and provides only the essential tools needed for web development. However, it's highly extensible through various third-party extensions.</li><br>
    <li><b>Routing:</b> Flask uses decorators to define routes easily. Routes map URL patterns to Python functions, allowing developers to handle different HTTP methods (GET, POST, etc.) and render templates.</li><br>
    <li><b>Jinja2 Templating:</b> Flask uses the Jinja2 templating engine, which enables creating HTML templates with placeholders for dynamic content. This separation of logic and presentation enhances code readability and maintainability.</li><br>
    <li><b>Flexible ORM Integration:</b> While not bundled with a specific ORM (Object-Relational Mapping), Flask seamlessly integrates with various ORMs like SQLAlchemy, allowing easy database interactions.</li><br>
    <li><b>Built-in Development Server:</b> Flask includes a built-in development server, making it convenient for local development and testing.</li><br>
    <li><b>RESTful Request Handling:</b> It allows easy implementation of RESTful APIs, making it suitable for building backend services.</li><br>
    <li><b>Extension Ecosystem:</b> Flask has a rich ecosystem of extensions that provide additional functionalities, such as Flask-RESTful for building APIs, Flask-SQLAlchemy for database integration, Flask-WTF for form handling, and many more.</li><br>
</ol>
<p>Flask is often chosen for various types of web projects due to its simplicity and flexibility. Its use cases include:</p>
<ul>
    <li><b>Web Applications:</b> Creating web applications of various sizes and complexities, from simple websites to more intricate applications.</li><br>
    <li><b>API Development:</b> Building RESTful APIs for client-server communication.</li><br>
    <li><b>Prototyping and MVPs:</b> Due to its quick setup and simplicity, Flask is often used for prototyping and building Minimum Viable Products (MVPs).</li><br>
</ul>

<h1>Jinja2 Template</h1>
<p>&nbsp; &nbsp; &nbsp; &nbsp;Jinja2 is a powerful and widely-used templating engine for Python, commonly integrated with web frameworks like Flask and Django. It allows developers to generate dynamic content by combining templates with data from Python code.</p><br>

<p>Key features and concepts of Jinja2 templates:</p>
<ol>
    <li><b>Template Inheritance:</b> Jinja2 supports template inheritance, enabling the creation of a base template with common elements (like headers, footers) that can be extended or overridden by child templates.</li><br>
    <li><b>Variable Substitution:</b> Jinja2 allows embedding variables within templates using double curly braces <b>&apos;{{ variable_name }}&apos;</b>. These placeholders are replaced with actual data when the template is rendered.</li><br>
    <li><b>Control Structures:</b> Jinja2 supports control structures such as loops (<b>&apos;{% for %}&apos;</b>), conditional statements (<b>&apos;{% if %}&apos;</b>), and blocks (<b>&apos;{% block %}&apos;</b>) to control the flow of content within templates.</li><br>
    <li><b>Template Extensions:</b> Jinja2 templates support extensions and custom filters, enabling developers to create reusable components or modify data output within templates.</li><br>
    <li><b>Comments:</b> Jinja2 allows commenting within templates using <b>&apos;{# Comment #}&apos;</b> syntax, allowing developers to add notes without affecting the rendered output.</li><br>
</ol>

<h1>templates</h1>
<p>&nbsp; &nbsp; &nbsp; &nbsp;Here, I used totally six templates. <b>&quot;Base.html&quot;</b> template is the base template</p>