<h1>Project</h1>
<p>	&nbsp;	&nbsp;	&nbsp;	&nbsp;In this project, You can view my blog, what I have posted but you can not change anything.</p>

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

<h1>Templates</h1>
<p>&nbsp; &nbsp; &nbsp; &nbsp;Here, I used totally six templates. <b>&quot;base.html&quot;</b> template is the base template for every other template. <b>&quot;home.html&quot;</b> template will display the all post in short along with date like when it was posted. If we click the heading that will show particular content in briefly in the <b>&quot;brief.html&quot;</b> template. And in <b>&quot;admin.html&quot;</b> template, User(Blog Owner) will log in into their account that will load the <b>&quot;adminpage.html&quot;</b> template, they can add, edit or delete their blog content in that template. By clicking edit button it will render <b>&quot;update.html&quot;</b> template to edit the content.</p><br>

<h1>PyMySQL Module</h1>
<p>&nbsp; &nbsp; &nbsp; &nbsp;The <b>&quot;pymysql&quot;</b> module is a Python client library used to interact with MySQL databases. It provides an interface for Python programs to connect to a MySQL server, execute SQL queries, and manage data within the database.</p><br>
<p>Key functionalities and features of <b>&apos;pymysql&apos;</b>:</p>
<ol>
    <li><b>Database Connection: &apos;pymysql &apos;</b> allows establishing connections to MySQL databases by providing methods to connect to a MySQL server using host, user, password, and database information.</li><br>
    <li><b>Executing Queries:</b> It enables executing SQL queries on the connected MySQL database using methods like <b>&apos;execute()&apos;</b> or <b>&apos;executemany()&apos;</b>. This allows for performing operations such as SELECT, INSERT, UPDATE, DELETE, and more.</li><br>
    <li><b>Fetching Results: &apos;pymysql&apos;</b> provides methods to fetch query results, allowing access to the retrieved data in various formats such as tuples, dictionaries, or custom data structures.</li><br>
    <li><b>Transactions:</b> It supports managing transactions by providing methods for committing changes (<b>&apos;commit( )&apos;</b>) or rolling back (<b>&apos;rollback( )&apos;</b>) changes made within a transaction.</li><br>
    <li><b>Parameterized Queries: &apos;pymysql&apos;</b> supports parameterized queries, which help prevent SQL injection by allowing the use of placeholders for query parameters</li><br>
</ol>