import React from 'react';

const InspectionItem = ({inspection}) => {
	return(
		<li className="list-group-item">
			<div><b>{inspection.inspection_date}</b></div>
			<div>{inspection.critical_flag}</div>
			<div>Score: {inspection.score}</div>
			<div>Grade: {inspection.grade}</div>
			<div>{inspection.grade_date}</div>
			<div>{inspection.action}</div>
			<div>Violation Code: {inspection.violation_code}</div>
			<div>{inspection.violation_description}</div>
		</li>
	);
}

export default InspectionItem;