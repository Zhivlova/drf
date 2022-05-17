import React from 'react'

const HeaderItem = ({header}) => {
    return (
        <tr>
            <td>
                {header.logo_icon}
            </td>
            <td>
                {header.logo_text}
            </td>
        </tr>
    )
}

const HeaderList = ({headers}) => {
    return (
        <table>
            <th>
                logo_icon
            </th>
            <th>
                logo_text
            </th>
            {headers.map((header) => <HeaderItem header={header} />)}
        </table>
    )
}

export default HeaderList