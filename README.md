<h1>Python auto update application setup</h1>

<h2>Pypudater init repository</h2>
<ul>
	<li>pyupdater keys -c</li>
	<li>pyupdater init</li>
	<li>pyupdater keys -i</li>pyupdater settings --plugin
	<li>pyupdater settings --plugin scp</li>
</ul>

<h2>Build new version and upload files</h2>
<ul>
	<li>pyupdater build --onefile --app-version=1.0.1 main.py</li>
	<li>pyupdater pkg --process --sign</li>
	<li>pyupdater upload --service scp</li>
</ul>

<p>The server can be as simple as an apache server on a raspberry pi.</p>