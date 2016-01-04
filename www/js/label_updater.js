/*
 * LABEL UPDATER for timelapse
 */
date = new Date();
currentHour = date.getHours();

function getCurrentDate() {
	document.write(date.getYear);
}

function getTorY(labelHour) {
	if (currentHour < labelHour) {
		document.write("yesterday");
	} else {
		document.write("today");
	}
}

function getDateShift(count) {
	if (currentHour < 8) {
		document.write((count + 1) + "days ago");
	} else {
		if (count == 0) {
			document.write("today");
		} else if (count == 1) {
			document.write("yesterday");
		} else {
			document.write(count + "days ago");
		}
	}
}
