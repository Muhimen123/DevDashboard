import dev_api
import data_reader
import data_writer
import graph


def help():
    print('============================')
    print('LIST OF AVAILABLE COMMANDS')
    print('============================')

    print("show-data >>> A bit described details for all your posts.")
    print("list-all >>> Short summary for all your posts.")
    print("show-data-single >>> A bit described details for a single post.")
    print("feed >>> Shows you a list of posts available in the feed")
    print("writedata >>> Writes data in a CSV file")

    print('\n\n^^^^^^^^^^^^^^^^^^^')
    print("NOW THE FUN PART")
    print('^^^^^^^^^^^^^^^^^^^\n\n')

    print("graph-bar >>> Histogram for all your post(including views, comments, reactions)")

    print("graph-bar-views >>> Histogram only for the post views")
    print("graph-bar-comments >>> Histogram only for the post comments")
    print("graph-bar-reactions >>> Histogram only for the post reactions")
    print("graph-bar-tags >>> Histogram for views per used tags")
    print("You can also try this: \tgraph-bar-reactions-comments")
    print("Protips: Try changing the attributes")

    print("\ngraph-progress >>> Shows a ojive curve for all of your post(including views, comments, reactions)")

    print("graph-progress-views >>> Ojive curve only for the post views")
    print("graph-progress-coments >>> Ojive curve only for the post comments")
    print("graph-progress-reactions >>> Ojive curve only for the post reactions")
    print("You can also try this: \tgraph-progress-reactions-comments")
    print("Protips: Try changing the attributes")

    print('\ngraph-pie-tags >>> Pie chart for used tags')

    print('\n')

    print('---------------------------')
    print("Boring part")
    print('---------------------------')
    print("help >>> shows the list of available commands")
    print("exit >>> closes the application")

    print('\nAll the commands are case incencitive\n')


cmd = 'pass'

while cmd.lower() != 'quit':
    cmd = input("==> ")
    
    if cmd.lower() == 'help':
        print('\n\n')
        help()

    elif cmd.lower() == 'show-data':
        print('\n\n')
        data_reader.show_data()

    elif cmd.lower() == 'feed':
        print('\n\n')
        data_reader.show_feed()

    elif cmd.lower() == 'list-all':
        print('\n\n')
        data_reader.list_all()

    elif cmd.lower() == 'show-data-single':
        print('\n\n')
        data_reader.show_data_singe()

    elif cmd.lower() == 'writedata':
        print('\n\n')
        data_writer.csv_writer()

    elif cmd.lower() == 'graph-bar':
        print('\n\n')
        graph.graph_bar()

    elif cmd.lower() == 'graph-bar-tags':
        print('\n\n')
        graph.graph_bar_tags()

    elif 'graph-bar-' in cmd.lower():
        print('\n\n')
        graph.graph_bar_filter(cmd.lower())

    elif cmd.lower() == 'graph-progress':
        print('\n\n')
        graph.graph_progress()

    elif cmd.lower() == 'graph-pie-tags':
        print('\n\n')
        graph.graph_pie_tags()

    elif cmd.lower() == 'exit':
        quit()

    elif 'graph-progress-' in cmd.lower():
        print('\n\n')
        graph.graph_progress_filter(cmd.lower())

    else:
        print('\n\n')
        print("No commands found.")
        print("Try typing 'help'")
