<html>
<h1>Server Log Details</h1>
<table border='2' bgcolor='green'>
<tr><td>IP</td><td>DATE</td><td>PICS</td><td>WEBSITE</td></tr>
%for i,j,k,l in res:
<tr><td>{{i}}</td><td>{{j}}</td><td>{{k}}</td><td>{{l}}</td></tr>
%end
</table>