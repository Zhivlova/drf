import React from 'react'

const TODOItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.uid}
            </td>
            <td>
                {item.todo_project}
            </td>
            <td>
                {item.text}
            </td>
            <td>
                {item.create_date}
            </td>
            <td>
                {item.update_date}
            </td>
            <td>
                {item.todo_user}
            </td>
        </tr>
    )
}

const TODOList = ({items}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Project
            </th>
            <th>
                Text
            </th>
            <th>
                Create date
            </th>
            <th>
                Update date
            </th>
            <th>
                User
            </th>
            {items.map((item) => <TODOList item={item} />)}
        </table>
    )
}

export default TODOList