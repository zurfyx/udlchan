class PostSorter:
    @staticmethod
    def sort(posts):
        """
        Sorts a list of Post objects and writes the nest level
        Use like sort(Post.objects.filter(main=<post>))
        :param posts: List of Post objects
        :return: sorted list with nest level
        """
        # sort taking parents into consideration
        # dict by parent
        parent_posts = {}
        for post in posts:
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
