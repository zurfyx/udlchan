class CommentSorter(object):
    @staticmethod
    def sort(comments):
        """
        Sorts a list of Post objects and writes the nest level
        Use like sort(Comment.objects.filter(topic=<topic>))
        :param posts: List of Comment objects
        :return: sorted list of Comment with nest level
        """
        # sort taking parents into consideration
        # dict by parent
        parent_posts = {}
        for post in comments:
            parent = post.parent
            if parent in parent_posts:
                parent_posts[parent].append(post)
            else:
                parent_posts[parent] = [post]

        # recursively generate tree
        def explore(source, parent_node, result, nest_level=0):
            if not parent_node in source: return
            for entry in source[parent_node]:
                entry.nest_level = nest_level
                result.append(entry)
                explore(source, entry, result, nest_level + 1)

        sorted_posts = []
        explore(parent_posts, None, sorted_posts)
        return sorted_posts
