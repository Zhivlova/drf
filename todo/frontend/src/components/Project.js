import React from 'react'

const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.uid}
            </td>
            <td>
                {item.title}
            </td>
            <td>
                {item.link}
            </td>
            <td>
                {item.project_users}
            </td>
        </tr>
    )
}

const ProjectList = ({items}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Title
            </th>
            <th>
                Link
            </th>
            <th>
                Users
            </th>
            {items.map((item) => <ProjectList item={item} />)}
        </table>
    )
}

export default ProjectList