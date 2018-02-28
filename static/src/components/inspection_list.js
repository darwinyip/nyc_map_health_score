import React from 'react';
import InspectionItem from './inspection_item'

const InspectionList = (props) => {
	const inspectionItems = props.inspections.map((inspection) => {
		return (
			<InspectionItem
				key={inspection.id}
				inspection={inspection} />
		);
	});

	return(
		<ul className="list-group">
			{inspectionItems}
		</ul>
	);
}

export default  InspectionList;