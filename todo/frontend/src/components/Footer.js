import React from 'react'

const FooterItem = ({footer}) => {
    return (
        <tr>
            <td>
                {footer.faq}
            </td>
            <td>
                {footer.contacts}
            </td>
            <td>
                {footer.copyright}
            </td>
        </tr>
    )
}

const FooterList = ({footers}) => {
    return (
        <table>
            <th>
                fag
            </th>
            <th>
                contacts
            </th>
             <th>
                copyright
            </th>
            {footers.map((footer) => <FooterItem footer={footer} />)}
        </table>
    )
}

export default FooterList