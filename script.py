import requests

response = requests.get("https://api.exchangeratesapi.io/2010-01-15")

print(response.json()["rates"])

rates = response.json()["rates"]

with open("table.html", "w") as file:
	file.write(
	"""<html>
	<head>
	<style>
	table, th, td {
	  border: 1px solid black;
	  border-collapse: collapse;
	}
	</style>
	</head>
	<body>""")
	file.write('<table style="width:100%">')
	file.write('<tr><th>Currency</th><th>Exchange rate (base EUR)</th></tr>')
	for key in response.json()["rates"]:
	 	file.write("<tr>")
	 	file.write(f"<td> {key} </td>")
	 	file.write(f"<td> {rates[key]} </td>")
	 	file.write("</tr>")

	file.write("</table></body></html>")
