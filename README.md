# asteroid_impact
Asteroid Impact is an open-source video game stimulus for conducting experimental research on human subjects.

<h1>License</h1>

Asteroid Impact was developed in the Media Neuroscience Lab (http://www.medianeuroscience.org/), Rene Weber, PI

Asteroid Impact is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see http://creativecommons.org/licenses/by-sa/4.0/.

Key Contributors include:

Nick Winters, Richard Huskey, Britney Craighead, Rene Weber

<h1>How to cite</h1>

If you use Asteroid Impact in your research, please cite:

Huskey, R., Craighead, B., Miller, M. B., Weber, R. (under review). <em>Intrinsic Reward Motivates Large-Scale Shifts BetweenCognitive Control and Default Mode Networks During Task Performance.</em>

We will update the citation once the manuscript is in press.

<h1>Introduction</h1>

<em>Asteroid Impact</em> is a point-and-click style video game where subjects use a cursor to collect crystal-shaped targets that are displayed at different locations while avoiding asteroids that bounce around the screen. Game difficulty is manipulated by altering the number of targets a subject needs to collect, the number of objects to be avoided, and the rate at which these objects move. The stimulus provides tremendous experimental control in that all random aspects of the game are removed; any differences in game experience are the result of player intervention. To help resolve this potential confound, the stimulus provides a high resolution content analysis of <em>all</em> events in the game (e.g., when a crystal is collected, x/y position of the player's cursor, time when player dies) with a 16ms temporal resolution. This content analysis is exported to a .csv file that allows for subsequent computation using a wide variety of analysis packages.

In terms of experimental manipulation, researchers can specify different levels of difficulty <em>a priori</em> as well as a time duration for how long a given level will last. <em>Asteroid Impact</em> also features an adaptive mode where the game automatically increases or decreases in difficulty depending on player performance. Each of these game states can be separated by a black screen or set of instructions. These different game states can be scripted together in any sequence the researcher may choose, thereby allowing the development of sophisticated experimental paradigms. The game's artwork can easily be manipulated and the game scales to fit in both full-screen and windowed modes across a variety of screen resolutions. The game is also designed to interface with TTL triggers, a feature which allows for synchronizing game states with psychophysiological and neurophysiological measurement equipment.

<em>Asteroid Impact</em> is written in Python and carries a fully open source license (CC BY-SA 4.0). This means that the game can be modified to suit the  needs of any given research lab. Moreover, the game is platform agnostic and can be used on Windows, OS X, or Linux (see known bugs below). The game requires minimal computational power and can run on low-cost computer systems. Taken together, these features provide the research community with a highly flexible tool that overcomes the issues discussed earlier. Moreover, the game conforms to the latest trends in open-science by providing a free tool that allows for replication.

<h1>Getting Started</h1>

Download and uncompress:
<ul>
<li>asteroid_impact_source_code.zip</li>
<li>asteroid_impact_documentation.zip</li>
</ul>

The documentation files specify necessary software dependencies and how to get <em>Asteroid Impact</em> running on your system.

<h1>! Known Issues</h1>

As with all experimental software, please use <em>Asteroid Impact</em> at your own risk, and after sufficient testing on your own hardware. The software does not come with any warranty. 

<em>Asteroid Impact</em> Has undergone extensive testing in Windows7, Windows10, and OS X 10.10.5 environments. Known bugs are listed below:
<ul>
<li>Trigger latency: TTL triggers connected with a USB or serial port experience a small latency depending on hardware. See the "Trigger Latency" section in the HTLM documentation for more details on how to test for this on your hardware.</li>
<li>Event Timer: When using OS X 10.10.5, the "total_millis" column in the .csv output does not tick correctly (not ticking every 16ms). This is due to a known limitation in PyGame 1.9.1 and we currently do not see a workaround for this issue. To our knowledge, the log records all game events, it is just that clock is not recording the timings correctly.</li>
</ul>
