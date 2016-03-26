import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Controls.Styles 1.3
import QtQuick.Layouts 1.1

Rectangle {
        width: 350
        height: 240
        TextField {
                id: input
                height: 30
                width: parent.width
                anchors.top: parent.top
                style: TextFieldStyle{
                        textColor: "black"

                        background: Rectangle {
                            radius: 2
                            border.color: "#333"
                            border.width: 1
                        }
                    }

            
            focus: true

            }


        GridLayout {
                id: grid
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.bottom: parent.bottom

                rows: 6
                columns: 4
                rowSpacing: 4
                columnSpacing: 4

                property double colMulti: grid.width/ grid.columns
                property double rowMulti: grid.height/ grid.rows

                function prefWidth(item){
                        return colMulti * item.Layout.columnSpan
                    }

                Button{
                        text: "("
                        onClicked: {
                                input.text += "("
                            }
                    }

                Button{
                        text: ")"
                        onClicked: {
                                input.text += ")"
                            }
                    }

                Button{
                        text: "sqrt"
                        onClicked: {
                                input.text += "~"
                            }
                    }

                Button{
                        text: "del"
                        onClicked: {
                                input.text = con.del_input(input.text)
                            }
                    }

                Button{
                        text: "%"
                        onClicked: {
                                input.text += "%"
                            }
                    }


                Button{
                        text: "^"
                        onClicked: {
                                input.text += "^"
                            }
                    }

                Button{
                        text: "C"
                        onClicked: {
                                input.text = ""
                            }
                    }

                Button{
                        text: "+"
                        onClicked: {

                                input.text += "+"
                            }
                    }

                Button{
                        text: "1"
                        onClicked: {
                                input.text += "1"
                            }
                    }

                Button{
                        text: "2"
                        onClicked: {
                                input.text += "2"
                            }
                    }

                Button{
                        text: "3"
                        onClicked: {
                                input.text += "3"
                            }
                    }

                Button{
                        text: "-"
                        onClicked: {
                                input.text += "-"
                            }
                    }

                Button{
                        text: "4"
                        onClicked: {
                                input.text += "4"
                            }
                    }

                Button{
                        text: "5"
                        onClicked: {
                                input.text += "5"
                            }
                    }

                Button{
                        text: "6"
                        onClicked: {
                                input.text += "6"
                            }
                    }

                Button{
                        text: "*"
                        onClicked: {
                                input.text += "*"
                            }
                    }

                Button{
                        text: "7"
                        onClicked: {
                                input.text += "7"
                            }
                    }

                Button{
                        text: "8"
                        onClicked: {
                                input.text += "8"
                            }
                    }

                Button{
                        text: "9"
                        onClicked: {
                                input.text += "9"
                            }
                    }

                Button{
                        text: "/"
                        onClicked: {
                                input.text += "/"
                            }
                    }

                Button{
                        text: "0"
                        onClicked: {
                                input.text += "0"
                            }
                    }

                Button{
                        id: dot
                        text: "."
                        onClicked: {
                                input.text += "."
                            }
                    }

                Button{
                        text: "="
                        onClicked: {
                                input.text = con.output(input.text)
                            }
                        Layout.columnSpan:2
                        Layout.preferredWidth: grid.prefWidth(this)


                    }
            
            }


    }
